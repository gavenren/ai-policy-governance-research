"""Reproduce transparent Canadian policy accounting cases, not forecasts."""
from pathlib import Path
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/inputs.json"
DATA = json.loads(INPUT.read_text())
O, A = DATA["official_inputs"], DATA["policy_assumptions"]
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)


def tax_package(cit_discount, gst_discount):
    cit = O["federal_cit"] * A["cit_surcharge_share_of_existing_liability"] * (1 - cit_discount)
    # This is a proportional approximation to net receipts, not a taxable-base estimate.
    gst = O["federal_gst"] * A["gst_rate_increase"] / O["gst_rate"] * (1 - gst_discount)
    rebate = A["new_annual_gst_rebate"]
    return {"cit_new": cit, "gst_new_before_extra_rebate": gst,
            "extra_rebate": rebate, "net_new_resources": cit + gst - rebate}


def transition(name, recipients, cit_discount, gst_discount, real_rate):
    tax = tax_package(cit_discount, gst_discount)
    debt = 0.0
    rows = []
    for i, year in enumerate(["2027-28", "2028-29", "2029-30", "2030-31", "2031-32"]):
        fraction = A["initial_year_receipts_fraction"] if i == 0 else 1.0
        income = A["initial_year_new_income_payments"] if i == 0 else recipients * A["transition_average_annual_payment"] / 1000
        needs = A["initial_year_needs_service_operation"] if i == 0 else A["transition_needs_and_service_operation"]
        admin = A["transition_annual_admin"]
        capital = A["transition_annual_capital_grants"]
        setup = A["transition_setup_once"] if i == 0 else 0.0
        reserve_add = A["transition_reserve_once"] if i == 0 else 0.0
        resources = tax["net_new_resources"] * fraction
        gross_tax = (tax["cit_new"] + tax["gst_new_before_extra_rebate"]) * fraction
        rebate = tax["extra_rebate"] * fraction
        primary_spending = income + needs + admin + capital + setup
        cash_gap_before_interest = primary_spending + reserve_add - resources
        # Conservative annual timing: charge a full year's real interest on opening
        # debt and on any positive primary financing need. Do not finance interest
        # on itself in this same annual period; carry it into the next year's debt.
        interest = real_rate * (debt + max(0, cash_gap_before_interest))
        deficit_change = primary_spending + rebate + interest - gross_tax
        financing = deficit_change + reserve_add
        closing = debt + financing
        assert closing >= 0, "Chosen case would need an explicit post-repayment cash rule."
        rows.append({"case": name, "year": year, "recipients_millions_full_year": recipients if i else 0,
                     "gross_new_tax": gross_tax, "extra_gst_rebate": rebate,
                     "net_new_resources": resources, "income_support": income,
                     "needs_services": needs, "admin": admin, "capital_grants": capital,
                     "setup": setup, "primary_spending_excluding_rebate": primary_spending,
                     "interest": interest, "deficit_change": deficit_change,
                     "reserve_added": reserve_add, "reserve_stock": A["transition_reserve_once"],
                     "opening_programme_debt": debt, "net_borrowing": financing,
                     "closing_programme_debt": closing,
                     "closing_net_debt_change": closing - A["transition_reserve_once"]})
        assert math.isclose(closing - debt, deficit_change + reserve_add, abs_tol=1e-10)
        debt = closing
    return rows


def full_loss(payment, pit_loss, gdp_multiple):
    adult = O["adult_population"] * payment / 1e9
    ccb_max = (O["children_under_6"] * O["ccb_under_6_max"]
               + O["children_6_to_17"] * O["ccb_6_to_17_max"]) / 1e9
    ccb_extra = ccb_max - O["ccb_baseline"]
    admin = adult * A["full_loss_admin_share_of_adult_payment"]
    spending = adult + ccb_extra + A["full_loss_new_service_cost"] + admin - A["full_loss_existing_benefit_savings"]
    lost_pit = O["federal_pit"] * pit_loss
    lost_ei = O["ei_premiums"] * A["full_loss_ei_premium_loss_share"]
    other_receipts = A["full_loss_other_existing_revenue_change"] + A["full_loss_new_payment_tax_recovery"]
    hold_deficit = spending + lost_pit + lost_ei - other_receipts
    balance_budget = hold_deficit + O["federal_deficit"]
    remaining_baseline_revenue = O["federal_revenue"] - lost_pit - lost_ei + other_receipts
    expense = O["federal_expense_after_actuarial_adjustment"] + spending
    assert math.isclose(expense - remaining_baseline_revenue, balance_budget, abs_tol=1e-8)
    return {"adult_annual_payment": payment, "pit_loss_share": pit_loss,
            "gdp_scale_multiple_only": gdp_multiple, "adult_gross_cost": adult,
            "ccb_total_maximum_case": ccb_max, "ccb_extra_over_baseline": ccb_extra,
            "new_service_cost": A["full_loss_new_service_cost"], "new_admin_cost": admin,
            "new_annual_spending": spending, "lost_federal_pit": lost_pit,
            "lost_ei_premiums": lost_ei, "remaining_baseline_revenue": remaining_baseline_revenue,
            "total_federal_expense": expense, "new_revenue_to_hold_old_deficit": hold_deficit,
            "new_revenue_to_balance_budget": balance_budget,
            "hold_deficit_requirement_pct_scaled_gdp": hold_deficit / (O["gdp_2026"] * gdp_multiple) * 100,
            "two_month_adult_payment_cash_buffer": adult / 6}


def write_csv(name, rows):
    with (OUT / name).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    assert A["transition_support_tax_free_and_disregarded_for_benefit_tests"]
    assert A["pre_april_2027_planning_uses_existing_department_budgets"]
    assert A["population_and_real_tax_bases_held_constant"]
    assert A["full_loss_assumes_all_counted_children_receive_current_ccb_maxima"]
    assert A["full_loss_payment_is_additional_tax_free_and_disregarded_for_benefit_tests"]
    assert A["reserve_real_return"] == 0, "This model has no reserve-return schedule."
    cit, gst = A["central_cit_receipt_discount"], A["central_gst_receipt_discount"]
    low_cit, low_gst = A["low_receipts_cit_discount"], A["low_receipts_gst_discount"]
    rate, n = A["real_borrowing_rate"], A["transition_adult_recipient_millions"]
    assumptions = [("central", cit, gst, rate, n), ("lower_receipts", low_cit, low_gst, rate, n),
                   ("double_recipients", cit, gst, rate, 2*n), ("higher_interest", cit, gst, 2*rate, n),
                   ("combined_adverse", low_cit, low_gst, 2*rate, 2*n)]
    transition_rows = [row for name, cit, gst, rate, n in assumptions
                       for row in transition(name, n, cit, gst, rate)]
    full_rows = [full_loss(p, loss, scale) for p in [18000, 24000, 30000]
                 for loss in [.5, .8, 1.] for scale in [1., 1.5, 2.]]
    central = full_loss(A["full_loss_adult_payment"], A["full_loss_pit_loss_share"], 1)
    taxes = [{"case": name, **tax_package(cit, gst)} for name, cit, gst
             in [("no_extra_discount", 0, 0), ("central", cit, gst), ("lower_receipts", low_cit, low_gst)]]
    write_csv("transition.csv", transition_rows)
    write_csv("full_loss.csv", full_rows)
    write_csv("funding.csv", taxes)
    summary = {"central_tax_package": taxes[1], "central_transition": transition_rows[:5],
               "central_full_loss": central, "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
               "checks": {"population_partition": O["adult_population"] + O["child_population"] == 41798407,
                          "child_partition": O["children_under_6"] + O["children_6_to_17"] == O["child_population"],
                          "cash_and_fiscal_accounts_reconcile": True,
                          "full_loss_baseline_reconciles": True},
               "case_counts": {"transition_rows": len(transition_rows), "full_loss_rows": len(full_rows),
                               "funding_rows": len(taxes)}}
    assert all(summary["checks"].values())
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
