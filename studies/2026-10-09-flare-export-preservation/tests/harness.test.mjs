import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { canonical, differencePaths, executeCases, loadUpstream, readPointer, same, verifyMinimalPairs, withFrozenClock, FROZEN_TIME } from '../code/run.mjs';

const fixtures = JSON.parse(readFileSync(new URL('../data/fixtures.json', import.meta.url), 'utf8'));
const upstream = await loadUpstream();
const clone = (value) => JSON.parse(JSON.stringify(value));

test('JSON pointers and equality keep absent, null, false and empty distinct', () => {
  assert.deepEqual(readPointer({}, '/x'), { state: 'missing' });
  assert.deepEqual(readPointer({ x: null }, '/x'), { state: 'present', value: null });
  assert.deepEqual(readPointer({ x: false }, '/x'), { state: 'present', value: false });
  assert.deepEqual(readPointer({ x: '' }, '/x'), { state: 'present', value: '' });
  assert.deepEqual(readPointer({ 'a/b': { '~c': [3] } }, '/a~1b/~0c/0'), { state: 'present', value: 3 });
  assert.ok(same({ b: 1, a: 2 }, { a: 2, b: 1 }));
  assert.ok(!same({}, { a: null }));
  assert.throws(() => readPointer({}, 'x'), /Invalid JSON pointer/);
});

test('clock is deterministic and restored on exceptions', () => {
  const nativeDate = globalThis.Date;
  assert.equal(withFrozenClock(() => new Date().toISOString()), FROZEN_TIME);
  assert.equal(withFrozenClock(() => Date.now()), Date.parse(FROZEN_TIME));
  assert.equal(withFrozenClock(() => new Date('2000-01-01T00:00:00Z').toISOString()), '2000-01-01T00:00:00.000Z');
  assert.throws(() => withFrozenClock(() => { throw new Error('test'); }), /test/);
  assert.equal(globalThis.Date, nativeDate);
});

test('minimal-pair guard rejects unrelated differences, identical records and query mismatch', () => {
  assert.deepEqual(differencePaths({ a: [1, 2] }, { a: [1, 3] }), ['/a/1']);
  verifyMinimalPairs(fixtures.cases);
  const pair = clone(fixtures.cases.slice(0, 2));
  pair[1].record.incidentDescription.issueDescription += ' unrelated';
  assert.throws(() => verifyMinimalPairs(pair), /must differ only/);
  pair[1].record = clone(pair[0].record);
  assert.throws(() => verifyMinimalPairs(pair), /must differ only/);
  pair[1].query_id = 'unrelated';
  assert.throws(() => verifyMinimalPairs(pair), /same declared query_id/);
});

test('upstream static and classification-dependent validators reject invalid input', () => {
  const invalidEmail = clone(fixtures.base_record);
  invalidEmail.reporterDetails.reporter.email = 'invalid';
  assert.equal(upstream.aiFlawReportSchema.safeParse(invalidEmail).success, false);
  const invalidHarm = clone(fixtures.base_record);
  invalidHarm.securityDetails.harmNarrative = '';
  assert.equal(upstream.aiFlawReportSchema.safeParse(invalidHarm).success, true);
  assert.equal(upstream.createAiFlawReportSchema({ csamInvolved: false, realWorldHarm: true, maliciousUse: false }).safeParse(invalidHarm).success, false);
  const result = executeCases({ cases: [{ id: 'invalid', record: invalidHarm }] }, upstream);
  assert.equal(result.cases[0].execution_status, 'not_converted_invalid_source_record');
  assert.equal(result.cases[0].outputs, undefined);
});

test('actual converter execution is deterministic and preserves every JSON-safe raw record', () => {
  const before = canonical(fixtures);
  const first = executeCases(fixtures, upstream);
  const second = executeCases(fixtures, upstream);
  assert.equal(canonical(first), canonical(second));
  assert.equal(canonical(fixtures), before);
  assert.equal(first.summary.valid_static, fixtures.cases.length);
  assert.equal(first.summary.valid_classification_dependent, fixtures.cases.length);
  assert.equal(first.summary.raw_round_trip_equal_cases, fixtures.cases.length);
  for (const item of first.cases) {
    assert.equal(item.outputs.jsonld.dateCreated, FROZEN_TIME);
    assert.ok(item.outputs.cert.vul_description.includes(FROZEN_TIME));
    assert.deepEqual(item.outputs.jsonld['flare:raw'], fixtures.cases.find((source) => source.id === item.id).record);
  }
});

test('version counterexample and raw-preserving negative control are measured separately', () => {
  const results = executeCases(fixtures, upstream);
  const versionPair = results.pairs.find((pair) => pair.id === 'P01');
  assert.equal(versionPair.distinguishable.jsonld, true);
  assert.equal(versionPair.distinguishable.jsonld_raw, true);
  assert.equal(versionPair.distinguishable.jsonld_named_projection, false);
  assert.equal(versionPair.distinguishable.cert, false);
  const source = fixtures.cases.find((item) => item.id === 'P01A').record;
  const result = results.cases.find((item) => item.id === 'P01A');
  assert.equal(result.outputs.jsonld.aiSystem[0].version, source.reporterDetails.systems[0].model);
  assert.notEqual(result.outputs.jsonld.aiSystem[0].version, source.reporterDetails.systems[0].version);
});

test('narrative distinction is not mislabeled as exact structured answer recovery', () => {
  const results = executeCases(fixtures, upstream);
  const cwePair = results.pairs.find((pair) => pair.id === 'P11');
  assert.equal(cwePair.distinguishable.cert, true);
  const cwe = results.cases.find((item) => item.id === 'P11A');
  assert.equal(cwe.query.cert.semantics, 'narrative');
  assert.equal(cwe.query.cert.exact_source_representation_equal, null);
  const disclosure = results.cases.find((item) => item.id === 'P13A');
  assert.equal(disclosure.query.jsonld_named.exact_source_representation_equal, false);
  assert.match(results.metadata.query_equality, /not semantic equivalence/);
});

test('nonempty attachments are outside the JSON-safe benchmark and rejected', () => {
  const record = clone(fixtures.base_record);
  record.evidence.attachments = [{ name: 'fake.pdf' }];
  assert.throws(() => executeCases({ cases: [{ id: 'attachment', record }] }, upstream), /empty-attachment/);
});
