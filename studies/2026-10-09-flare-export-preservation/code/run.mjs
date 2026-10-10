#!/usr/bin/env node
/** Execute unchanged, pinned FLARE-AI converters and validators on JSON fixtures. */
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { createRequire, registerHooks } from 'node:module';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export const PINNED_COMMIT = 'f51514d4b999fa7988e05d44b9bf18ea0aa98031';
export const FROZEN_TIME = '2026-10-09T00:00:00.000Z';
const here = path.dirname(fileURLToPath(import.meta.url));
const workspace = path.resolve(here, '../../..');
const defaultSource = path.join(workspace, '.local-sources/prior-art/flare-code');
const defaultDependencies = path.join(workspace, '.local-tools/flare-harness');
const modelDir = 'client/src/entities/ai-flaw-report/model';
const converterDir = 'client/src/entities/ai-flaw-report/lib';
const zipHookPath = `${modelDir}/hooks/useDownloadReport.ts`;
const pinnedDependencies = { zod: '4.3.6', next: '16.1.6', react: '19.2.4', 'react-dom': '19.2.4' };

export const sha256 = (value) => createHash('sha256').update(value).digest('hex');
export function canonical(value) {
  if (Array.isArray(value)) return `[${value.map(canonical).join(',')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonical(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}
const jsonCopy = (value) => JSON.parse(JSON.stringify(value));
export const same = (a, b) => canonical(a) === canonical(b);

/** JSON leaf differences; an absent property differs from any present value. */
export function differencePaths(a, b, prefix = '') {
  if (same(a, b)) return [];
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object' || Array.isArray(a) !== Array.isArray(b)) return [prefix];
  const differences = [];
  for (const key of [...new Set([...Object.keys(a), ...Object.keys(b)])].sort()) {
    const pointer = `${prefix}/${key.replaceAll('~', '~0').replaceAll('/', '~1')}`;
    if (!Object.hasOwn(a, key) || !Object.hasOwn(b, key)) differences.push(pointer);
    else differences.push(...differencePaths(a[key], b[key], pointer));
  }
  return differences;
}

export function verifyMinimalPairs(cases) {
  const grouped = new Map();
  for (const item of cases) if (item.pair_id) grouped.set(item.pair_id, [...(grouped.get(item.pair_id) ?? []), item]);
  for (const [id, items] of grouped) {
    if (items.length !== 2) throw new Error(`Pair ${id} must contain exactly two cases.`);
    const [a, b] = items;
    if (!a.query_id || a.query_id !== b.query_id) throw new Error(`Pair ${id} must have the same declared query_id.`);
    if (!a.source_path || a.source_path !== b.source_path) throw new Error(`Pair ${id} must have the same declared source_path.`);
    const differences = differencePaths(a.record, b.record);
    if (differences.length !== 1 || differences[0] !== a.source_path) throw new Error(`Pair ${id} must differ only at ${a.source_path}; actual differences: ${differences.join(', ')}`);
  }
}

/** Preserve missing/null/false/empty distinctions, including escaped JSON pointer keys. */
export function readPointer(value, pointer) {
  if (pointer === '') return { state: 'present', value };
  if (typeof pointer !== 'string' || !pointer.startsWith('/')) throw new Error(`Invalid JSON pointer: ${pointer}`);
  let current = value;
  for (const key of pointer.slice(1).split('/').map((part) => part.replaceAll('~1', '/').replaceAll('~0', '~'))) {
    if (current === null || typeof current !== 'object' || !Object.hasOwn(current, key)) return { state: 'missing' };
    current = current[key];
  }
  return { state: 'present', value: current };
}

/** Synchronous global clock override; restored even when conversion throws. */
export function withFrozenClock(fn, timestamp = FROZEN_TIME) {
  const OriginalDate = globalThis.Date;
  const instant = OriginalDate.parse(timestamp);
  if (!Number.isFinite(instant)) throw new Error('Frozen timestamp must be a valid ISO date.');
  class FixedDate extends OriginalDate {
    constructor(...args) { super(...(args.length ? args : [instant])); }
    static now() { return instant; }
  }
  globalThis.Date = FixedDate;
  try {
    const value = fn();
    if (value && typeof value.then === 'function') throw new Error('Clock scope must be synchronous.');
    return value;
  } finally {
    globalThis.Date = OriginalDate;
  }
}

function packageVersions(dependenciesRoot) {
  const versions = {};
  for (const [name, expected] of Object.entries(pinnedDependencies)) {
    const actual = JSON.parse(readFileSync(path.join(dependenciesRoot, 'node_modules', name, 'package.json'), 'utf8')).version;
    if (actual !== expected) throw new Error(`Expected ${name}@${expected}; found ${actual}.`);
    versions[name] = actual;
  }
  return versions;
}

/** Runtime resolution only: no upstream source text is rewritten, stubbed or copied. */
export async function loadUpstream({ sourceRoot = defaultSource, dependenciesRoot = defaultDependencies } = {}) {
  sourceRoot = path.resolve(sourceRoot);
  dependenciesRoot = path.resolve(dependenciesRoot);
  const dependencyVersions = packageVersions(dependenciesRoot);
  const dependencyRequire = createRequire(path.join(dependenciesRoot, 'package.json'));
  const imported = new Set();
  const sourcePrefix = `${sourceRoot}${path.sep}`;
  const resolveOriginal = (absolute) => {
    for (const candidate of [absolute, `${absolute}.ts`, `${absolute}.js`, path.join(absolute, 'index.ts')]) {
      if (existsSync(candidate) && path.extname(candidate)) return pathToFileURL(candidate).href;
    }
    throw new Error(`Unresolved upstream import: ${path.relative(sourceRoot, absolute)}`);
  };
  const hooks = registerHooks({
    resolve(specifier, context, nextResolve) {
      if (specifier === 'zod' || specifier === 'next/dynamic') {
        return nextResolve(pathToFileURL(dependencyRequire.resolve(specifier)).href, context);
      }
      if (specifier.startsWith('~/')) return nextResolve(resolveOriginal(path.join(sourceRoot, 'client/src', specifier.slice(2))), context);
      if (specifier.startsWith('.') && context.parentURL?.startsWith(pathToFileURL(sourceRoot).href)) {
        return nextResolve(resolveOriginal(fileURLToPath(new URL(specifier, context.parentURL))), context);
      }
      return nextResolve(specifier, context);
    },
    load(url, context, nextLoad) {
      if (url.startsWith('file:')) {
        const absolute = fileURLToPath(url);
        if (absolute.startsWith(sourcePrefix)) imported.add(path.relative(sourceRoot, absolute).split(path.sep).join('/'));
      }
      return nextLoad(url, context);
    },
  });
  let converter, cert, schemas;
  try {
    // This entry order resolves the original schema/constants ESM cycle without modifying it.
    await import(pathToFileURL(path.join(sourceRoot, modelDir, 'constants.ts')).href);
    schemas = await import(pathToFileURL(path.join(sourceRoot, modelDir, 'schema.ts')).href);
    converter = await import(pathToFileURL(path.join(sourceRoot, converterDir, 'jsonld-converter.ts')).href);
    cert = await import(pathToFileURL(path.join(sourceRoot, converterDir, 'cert-converter.ts')).href);
  } finally {
    hooks.deregister();
  }
  // Fixed manifest remains complete if a caller loads the same cached ESM modules again.
  const sourceFiles = [...new Set([...imported,
    'LICENSE', 'yarn.lock', 'client/package.json', 'client/src/lib/hash.ts', 'client/src/lib/url.ts',
    `${converterDir}/jsonld-converter.ts`, `${converterDir}/cert-converter.ts`,
    `${modelDir}/schema.ts`, `${modelDir}/constants.ts`, `${modelDir}/step-config.ts`,
    `${modelDir}/form-data/disclosure-plan-fields-config.ts`,
    `${modelDir}/form-data/impact-assessment-fields-config.ts`,
    `${modelDir}/form-data/security-details-fields-config.ts`,
    `${modelDir}/form-data/incident-description-fields-config.ts`,
    `${modelDir}/form-data/reporter-details-data.ts`,
    'client/src/widgets/ai-flaw-report/reporter-details-step/ai-system-info.tsx', zipHookPath,
  ])].sort();
  const sourceHashes = Object.fromEntries(sourceFiles.map((name) => [name, sha256(readFileSync(path.join(sourceRoot, name)))]));
  let verification;
  try {
    const actual = execFileSync('git', ['-C', sourceRoot, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    if (actual !== PINNED_COMMIT) throw new Error(`Unexpected upstream commit: ${actual}`);
    for (const name of sourceFiles) {
      const committed = execFileSync('git', ['-C', sourceRoot, 'show', `${PINNED_COMMIT}:${name}`], { maxBuffer: 10 * 1024 * 1024 });
      if (sha256(committed) !== sourceHashes[name]) throw new Error(`Upstream source differs from pinned commit: ${name}`);
    }
    verification = 'All listed source bytes verified against pinned Git commit.';
  } catch (error) {
    // Refuse an unverified checkout: a source hash alone is not a commit attestation.
    throw new Error(`Pinned-source verification failed: ${error.message}`, { cause: error });
  }
  const localLock = path.join(dependenciesRoot, 'package-lock.json');
  return {
    convertToJsonLd: converter.convertToJsonLd,
    convertToCert: cert.convertToCert,
    aiFlawReportSchema: schemas.aiFlawReportSchema,
    createAiFlawReportSchema: schemas.createAiFlawReportSchema,
    metadata: {
      repository: 'https://github.com/ai-flaw-reporting/ai-flaw-reporting',
      commit: PINNED_COMMIT,
      verification,
      source_sha256: sourceHashes,
      direct_dependency_versions: dependencyVersions,
      dependency_lock_sha256: existsSync(localLock) ? sha256(readFileSync(localLock)) : null,
      runtime: { node: process.version, upstream_node_engine: '>=20.0.0 <=22.x.x', in_declared_range: [20, 21, 22].includes(Number(process.versions.node.split('.')[0])), type_execution: 'Node native TypeScript stripping; runtime alias and extension resolution only' },
      import_order: 'constants.ts before schema.ts; actual next/dynamic dependency loaded; no UI rendering',
      zip_control: { status: 'static inspection only; original download hook not executed', source_path: zipHookPath, observation: 'Hook writes original non-file fields to report.json, removes evidence.attachments and adds their contents separately under attachments/. This harness does not claim ZIP packaging, browser or attachment fidelity.' },
    },
  };
}

function validate(schema, record) {
  const result = schema.safeParse(record);
  if (!result.success) return { valid: false, issues: jsonCopy(result.error.issues) };
  return { valid: true, parsed_differs_from_input: !same(record, result.data), parsed_sha256: sha256(canonical(result.data)) };
}

function queryObservations(record, jsonld, cert, query = {}) {
  const paths = query.profile_paths ?? {};
  const sourcePaths = query.source_paths ?? [];
  const values = (object, pointers) => pointers.map((pointer) => ({ pointer, ...readPointer(object, pointer) }));
  const source = values(record, sourcePaths);
  const result = { source };
  for (const [profile, object] of [['jsonld_named', jsonld], ['cert', cert]]) {
    const observations = values(object, paths[profile] ?? []);
    const semantics = query.profile_semantics?.[profile] ?? 'unspecified';
    result[profile] = {
      semantics,
      observations,
      // Literal representation only, NOT semantic equivalence: no -> No is false.
      // No decoder or natural-language inference is applied.
      exact_source_representation_equal: semantics === 'structured' && source.length === 1 && observations.length === 1
        ? same({ ...source[0], pointer: '' }, { ...observations[0], pointer: '' }) : null,
    };
  }
  return result;
}

export function executeCases(fixtures, upstream, { frozenTime = FROZEN_TIME } = {}) {
  if (!Array.isArray(fixtures.cases) || !fixtures.cases.length) throw new Error('Fixture input must contain a nonempty cases array.');
  verifyMinimalPairs(fixtures.cases);
  const queries = new Map((fixtures.queries ?? []).map((query) => [query.id, query]));
  if (queries.size !== (fixtures.queries ?? []).length) throw new Error('Query ids must be unique.');
  for (const item of fixtures.cases) {
    if (item.pair_id && (!queries.has(item.query_id) || !queries.get(item.query_id).source_paths?.includes(item.source_path))) {
      throw new Error(`Paired case ${item.id} must reference a defined query containing its source_path.`);
    }
  }
  const ids = new Set();
  const results = fixtures.cases.map((item) => {
    if (!item.id || ids.has(item.id)) throw new Error(`Missing or duplicate case id: ${item.id}`);
    ids.add(item.id);
    const record = jsonCopy(item.record);
    if ((record.evidence?.attachments ?? []).length) throw new Error(`Case ${item.id}: only JSON-safe, empty-attachment records are supported.`);
    const inputHash = sha256(canonical(record));
    const classify = record.classifyReport ?? {};
    const staticValidation = validate(upstream.aiFlawReportSchema, record);
    const dynamicValidation = validate(upstream.createAiFlawReportSchema({ csamInvolved: classify.csam_involved, realWorldHarm: classify.real_world_harm, maliciousUse: classify.malicious_use }), record);
    const base = { id: item.id, pair_id: item.pair_id ?? null, query_id: item.query_id ?? item.query?.id ?? null, source_path: item.source_path ?? null, expected: item.expected ?? null, input_sha256: inputHash, validation: { static: staticValidation, classification_dependent: dynamicValidation } };
    if (!staticValidation.valid || !dynamicValidation.valid) return { ...base, execution_status: 'not_converted_invalid_source_record' };
    const { jsonld, cert } = withFrozenClock(() => ({
      jsonld: JSON.parse(upstream.convertToJsonLd(record, { createdAt: frozenTime, schemaVersion: '1.0' })),
      cert: JSON.parse(upstream.convertToCert(record)),
    }), frozenTime);
    if (sha256(canonical(record)) !== inputHash) throw new Error(`Converter mutated input in ${item.id}.`);
    const { 'flare:raw': raw, ...named } = jsonld;
    const query = queries.get(base.query_id) ?? item.query ?? {};
    return { ...base, execution_status: 'converted', raw_round_trip_equal: same(record, raw), output_sha256: { jsonld: sha256(canonical(jsonld)), jsonld_named_projection: sha256(canonical(named)), jsonld_raw: sha256(canonical(raw)), cert: sha256(canonical(cert)) }, query: queryObservations(record, named, cert, query), outputs: { jsonld, cert } };
  });
  const grouped = new Map();
  for (const result of results) {
    if (result.pair_id) grouped.set(result.pair_id, [...(grouped.get(result.pair_id) ?? []), result]);
  }
  const pairs = [...grouped].map(([id, items]) => {
    if (items.length !== 2) throw new Error(`Pair ${id} must contain exactly two cases.`);
    const [a, b] = items;
    const base = { id, cases: [a.id, b.id], query_id: a.query_id, changed_leaf: a.source_path, minimal_pair_verified: true, source_records_distinct: a.input_sha256 !== b.input_sha256 };
    if (items.some((item) => item.execution_status !== 'converted')) return { ...base, status: 'invalid_source_record', distinguishable: null };
    const distinguishable = Object.fromEntries(Object.keys(a.output_sha256).map((key) => [key, a.output_sha256[key] !== b.output_sha256[key]]));
    return { ...base, status: 'executed', distinguishable, query_observations_distinct: { source: !same(a.query.source, b.query.source), jsonld_named: !same(a.query.jsonld_named.observations, b.query.jsonld_named.observations), cert: !same(a.query.cert.observations, b.query.cert.observations) } };
  });
  const executed = pairs.filter((pair) => pair.status === 'executed');
  const count = (predicate) => results.filter(predicate).length;
  return {
    metadata: { ...upstream.metadata, frozen_time: frozenTime, input_representation: 'Unmodified JSON fixture record, after validation; schema-parsed defaults are not substituted.', equality: 'Canonical JSON structural equality; named projection removes only flare:raw from actual JSON-LD output.', query_equality: 'exact_source_representation_equal is literal representation equality, not semantic equivalence or answer correctness. For example no -> No yields false. No semantic decoder was applied.', minimal_pairs: 'Every pair has exactly two cases, one query_id, one source_path and exactly one differing JSON leaf at that path.', scope: 'Synthetic configuration counterexamples; no frequency, operational benefit, legal compliance or UI conformance inference.' },
    summary: { case_count: results.length, valid_static: count((item) => item.validation.static.valid), valid_classification_dependent: count((item) => item.validation.classification_dependent.valid), converted_cases: count((item) => item.execution_status === 'converted'), raw_round_trip_equal_cases: count((item) => item.raw_round_trip_equal), pair_count: pairs.length, executed_pairs: executed.length, distinguished_pair_counts: Object.fromEntries(['jsonld', 'jsonld_named_projection', 'jsonld_raw', 'cert'].map((profile) => [profile, executed.filter((pair) => pair.distinguishable[profile]).length])) },
    pairs, cases: results,
  };
}

export function summaryCsv(result) {
  const header = ['pair_id', 'query_id', 'changed_leaf', 'minimal_pair_verified', 'full_jsonld_distinct', 'jsonld_raw_distinct', 'jsonld_named_projection_distinct', 'standalone_cert_distinct', 'source_query_distinct', 'jsonld_named_query_distinct', 'cert_query_distinct'];
  const rows = result.pairs.map((pair) => [pair.id, pair.query_id, pair.changed_leaf, pair.minimal_pair_verified, pair.distinguishable?.jsonld, pair.distinguishable?.jsonld_raw, pair.distinguishable?.jsonld_named_projection, pair.distinguishable?.cert, pair.query_observations_distinct?.source, pair.query_observations_distinct?.jsonld_named, pair.query_observations_distinct?.cert]);
  const cell = (value) => `"${String(value ?? '').replaceAll('"', '""')}"`;
  return `${[header, ...rows].map((row) => row.map(cell).join(',')).join('\n')}\n`;
}

async function main() {
  const startedUtc = new Date().toISOString();
  const args = process.argv.slice(2);
  const option = (name, fallback) => { const i = args.indexOf(name); return i === -1 ? fallback : args[i + 1]; };
  if (args.includes('--help')) {
    console.log('node code/run.mjs --fixtures data/fixtures.json [--out results/results.json] [--execution-log results/execution.json] [--summary-csv results/summary.csv] [--source-manifest results/source-manifest.json] [--source-root PATH] [--dependencies-root PATH]');
    return;
  }
  const inputPath = path.resolve(option('--fixtures', path.join(here, '../data/fixtures.json')));
  const inputBytes = readFileSync(inputPath);
  const fixtures = JSON.parse(inputBytes);
  const upstream = await loadUpstream({ sourceRoot: option('--source-root', defaultSource), dependenciesRoot: option('--dependencies-root', defaultDependencies) });
  const result = executeCases(fixtures, upstream);
  result.metadata.fixture_file_sha256 = sha256(inputBytes);
  result.metadata.harness_sha256 = sha256(readFileSync(fileURLToPath(import.meta.url)));
  const output = `${JSON.stringify(result, null, 2)}\n`;
  const outputPath = option('--out');
  if (outputPath) { mkdirSync(path.dirname(path.resolve(outputPath)), { recursive: true }); writeFileSync(outputPath, output); }
  else process.stdout.write(output);
  const summaryPath = option('--summary-csv');
  if (summaryPath) {
    mkdirSync(path.dirname(path.resolve(summaryPath)), { recursive: true });
    writeFileSync(summaryPath, summaryCsv(result));
  }
  const manifestPath = option('--source-manifest');
  if (manifestPath) {
    mkdirSync(path.dirname(path.resolve(manifestPath)), { recursive: true });
    writeFileSync(manifestPath, `${JSON.stringify({ repository: upstream.metadata.repository, commit: upstream.metadata.commit, verification: upstream.metadata.verification, source_sha256: upstream.metadata.source_sha256 }, null, 2)}\n`);
  }
  const logPath = option('--execution-log');
  if (logPath) {
    const log = { started_utc: startedUtc, completed_utc: new Date().toISOString(), timestamp_source: 'Host wall clock outside the synchronous synthetic Date override', result_sha256: sha256(output), fixture_sha256: result.metadata.fixture_file_sha256, harness_sha256: result.metadata.harness_sha256, node: process.version, summary: result.summary };
    mkdirSync(path.dirname(path.resolve(logPath)), { recursive: true });
    writeFileSync(logPath, `${JSON.stringify(log, null, 2)}\n`);
  }
  if (result.summary.converted_cases !== result.summary.case_count) process.exitCode = 2;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => { console.error(error.stack); process.exitCode = 1; });
}
