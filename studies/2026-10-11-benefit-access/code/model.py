"""S007: deterministic denied-claim queue and payment accounting; stdlib only."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import csv
import hashlib
import json
import platform

STUDY = Path(__file__).resolve().parents[1]
TOL = 1e-8

def simulate(eligible, denied, ineligible, capacity, recovery=0.5, benefit=1.0,
             review_slot_cost=0.0, deadline=2):
    """Arrive, advance (P only), review FIFO, settle; observe at period end.

    Eligible funding arrives when due. All ineligible arrivals enter the denied
    queue. Within each date cohort, service is proportional to its two masses.
    Recovery occurs only for reviewed ineligible claims; no eligible clawback.
    """
    n = len(eligible)
    if n == 0 or any(len(x) != n for x in (denied, ineligible, capacity)):
        raise ValueError('nonempty equal-length inputs are required')
    if not 0 <= recovery <= 1 or benefit <= 0 or review_slot_cost < 0:
        raise ValueError('invalid monetary parameter')
    if isinstance(deadline, bool) or not isinstance(deadline, int) or deadline < 0:
        raise ValueError('deadline must be a nonnegative integer')
    for nt, et, it, mt in zip(eligible, denied, ineligible, capacity):
        if min(nt, et, it, mt) < 0 or et > nt:
            raise ValueError('invalid arrival or capacity')
    queue, rows = [], []
    total_n = total_e = total_i = done_e = done_i = slots = 0.0
    delay = late = missed_deadline = 0.0
    deadline_advanced_i = deadline_recovered_cases = 0.0
    for t, (nt, et, it, mt) in enumerate(zip(eligible, denied, ineligible, capacity), 1):
        total_n += nt
        total_e += et
        total_i += it
        slots += mt
        # Base entitlement cash is available before advances. Recovery follows.
        gross_extra = benefit * (total_i - recovery * done_i)
        if et + it > 0:
            queue.append({'arrival': t, 'e': float(et), 'i': float(it)})
        remaining = float(mt)
        period_e = period_i = previously_advanced_i = 0.0
        while remaining > TOL and queue:
            cohort = queue[0]
            mass = cohort['e'] + cohort['i']
            served = min(remaining, mass)
            share = served / mass
            se, si = cohort['e'] * share, cohort['i'] * share
            cohort['e'] -= se
            cohort['i'] -= si
            period_e += se
            period_i += si
            if cohort['arrival'] < t:
                previously_advanced_i += si
            remaining -= served
            if cohort['e'] + cohort['i'] <= TOL:
                queue.pop(0)
        done_e += period_e
        done_i += period_i
        qe = sum(x['e'] for x in queue)
        qi = sum(x['i'] for x in queue)
        delay += qe
        late += sum(x['e'] for x in queue if x['arrival'] == t)
        missed_deadline += sum(x['e'] for x in queue if x['arrival'] + deadline == t)
        # Deadline advances only pay claims still open after that period's review.
        # Same-period ineligible resolutions get no advance under this rule.
        deadline_advanced_i += sum(x['i'] for x in queue if x['arrival'] == t)
        deadline_gross = benefit*(deadline_advanced_i - recovery*deadline_recovered_cases)
        deadline_recovered_cases += previously_advanced_i
        deadline_extra = benefit*(deadline_advanced_i - recovery*deadline_recovered_cases)
        review_cost = review_slot_cost * slots
        due_funding = benefit * total_n + review_cost
        appeal_outflow = benefit * (total_n - total_e + done_e) + review_cost
        advance_outflow = benefit * (total_n + total_i - recovery * done_i) + review_cost
        net_extra = advance_outflow - due_funding
        loss_to_date = benefit * (1 - recovery) * done_i
        row = dict(period=t, eligible_due=nt, eligible_denied=et, ineligible_arrivals=it,
                   capacity=mt, reviewed_eligible=period_e, reviewed_ineligible=period_i,
                   backlog_eligible=qe, backlog_ineligible=qi, delay_claim_periods=delay,
                   late_eligible_claims=late, deadline_misses=missed_deadline,
                   eligible_funding_plus_review=due_funding,
                   appeal_net_outflow=appeal_outflow, advance_net_outflow=advance_outflow,
                   appeal_earmarked_cash=due_funding-appeal_outflow,
                   extra_cash_net=net_extra, extra_cash_gross=gross_extra,
                   spending_gap=advance_outflow-appeal_outflow,
                   permanent_loss_resolved=loss_to_date,
                   unresolved_ineligible_gross=benefit*qi,
                   eventual_loss_all_arrivals=benefit*(1-recovery)*total_i)
        row.update(deadline_extra_cash_net=deadline_extra,
                   deadline_extra_cash_gross=deadline_gross,
                   deadline_ineligible_advanced=deadline_advanced_i,
                   deadline_ineligible_reviewed_after_advance=deadline_recovered_cases,
                   deadline_eventual_loss=benefit*(1-recovery)*deadline_advanced_i)
        # Internal accounting checks are not independent validation.
        assert abs(total_e - done_e - qe) < TOL
        assert abs(total_i - done_i - qi) < TOL
        assert abs(net_extra - benefit*(qi+(1-recovery)*done_i)) < TOL
        assert abs(row['spending_gap'] - benefit*qe - net_extra) < TOL
        assert abs(deadline_extra-benefit*(qi+(1-recovery)*deadline_recovered_cases)) < TOL
        assert deadline_extra <= net_extra+TOL
        assert period_e + period_i <= mt + TOL
        rows.append(row)
    last = rows[-1]
    summary = dict(eligible_claims=total_n, eligible_denied=total_e,
                   ineligible_claims=total_i, available_review_slots=slots,
                   reviewed_eligible=done_e, reviewed_ineligible=done_i,
                   late_eligible_claims=late, late_share_all_eligible=late/total_n if total_n else 0,
                   delay_claim_periods=delay, deadline_misses=missed_deadline,
                   terminal_eligible_arrears=benefit*last['backlog_eligible'],
                   terminal_ineligible_open=benefit*last['backlog_ineligible'],
                   terminal_extra_cash_net=last['extra_cash_net'],
                   peak_extra_cash_net=max(x['extra_cash_net'] for x in rows),
                   peak_extra_cash_gross=max(x['extra_cash_gross'] for x in rows),
                   permanent_loss_resolved=last['permanent_loss_resolved'],
                   eventual_loss_all_arrivals=last['eventual_loss_all_arrivals'],
                   peak_spending_gap=max(x['spending_gap'] for x in rows))
    summary.update(deadline_peak_extra_cash_net=max(x['deadline_extra_cash_net'] for x in rows),
                   deadline_peak_extra_cash_gross=max(x['deadline_extra_cash_gross'] for x in rows),
                   deadline_eventual_loss=last['deadline_eventual_loss'])
    return rows, summary

def expand(spec, horizon):
    eligible = [spec.get('eligible_per_period', 100)] * horizon
    denied = [spec['base_denials']] * horizon
    invalid = [spec['ineligible_per_period']] * horizon
    capacity = [spec['capacity']] * horizon
    start = spec.get('shock_start', 4)
    for period in range(start, start + spec.get('shock_length', 0)):
        denied[period-1] = spec.get('shock_denials', spec['base_denials'])
        capacity[period-1] = spec.get('shock_capacity', 0)
    if 'denial_path' in spec:
        denied = spec['denial_path']
    if 'capacity_path' in spec:
        capacity = spec['capacity_path']
    return eligible, denied, invalid, capacity

def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    design_path = STUDY / 'data/design.json'
    raw = design_path.read_bytes()
    design = json.loads(raw)
    results = STUDY / 'results'
    results.mkdir(exist_ok=True)
    scenarios, trajectories = [], []
    for spec in design['scenarios']:
        rows, summary = simulate(*expand(spec, design['horizon']), recovery=spec['recovery'],
                                 benefit=design['benefit'], deadline=design['deadline'])
        scenarios.append(dict(scenario=spec['name'], **summary))
        trajectories.extend(dict(scenario=spec['name'], **r) for r in rows)
    write_csv(results / 'scenarios.csv', scenarios)
    write_csv(results / 'trajectories.csv', trajectories)
    grid = design['grid']
    keys = list(grid)
    stress, seen = [], set()
    for ix, values in enumerate(product(*(grid[k] for k in keys)), 1):
        spec = dict(zip(keys, values))
        paths = expand(spec, design['horizon'])
        signature = (tuple(tuple(x) for x in paths), spec['recovery'])
        if signature in seen:
            continue
        seen.add(signature)
        _, summary = simulate(*paths, recovery=spec['recovery'],
                              benefit=design['benefit'], deadline=design['deadline'])
        stress.append(dict(case=ix, **spec, **summary))
    write_csv(results / 'stress.csv', stress)
    net_pass = sum(x['peak_extra_cash_net'] <= design['reserve']+TOL for x in stress)
    gross_pass = sum(x['peak_extra_cash_gross'] <= design['reserve']+TOL for x in stress)
    timely = sum(x['late_eligible_claims'] <= TOL for x in stress)
    deadline_net_pass = sum(x['deadline_peak_extra_cash_net'] <= design['reserve']+TOL for x in stress)
    deadline_gross_pass = sum(x['deadline_peak_extra_cash_gross'] <= design['reserve']+TOL for x in stress)
    summary = dict(cases=len(stress), reserve=design['reserve'], net_reserve_pass=net_pass,
                   gross_reserve_pass=gross_pass, appeal_all_timely=timely,
                   deadline_net_reserve_pass=deadline_net_pass,
                   deadline_gross_reserve_pass=deadline_gross_pass,
                   max_delay_claim_periods=max(x['delay_claim_periods'] for x in stress),
                   max_peak_extra_cash_net=max(x['peak_extra_cash_net'] for x in stress),
                   max_peak_extra_cash_gross=max(x['peak_extra_cash_gross'] for x in stress))
    (results/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    output_names = ['scenarios.csv','trajectories.csv','stress.csv','summary.json']
    metadata = dict(run_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    python=platform.python_version(), platform=platform.system(),
                    design_sha256=hashlib.sha256(raw).hexdigest(),
                    model_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    deterministic_outputs={name:hashlib.sha256((results/name).read_bytes()).hexdigest() for name in output_names},
                    random_seed=None, random_sampling=False, exit_status=0)
    (results/'run.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    main()
