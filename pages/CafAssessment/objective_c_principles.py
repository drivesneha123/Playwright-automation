from playwright.sync_api import Page
from pages.CafAssessment import outcome_page


def complete_objective_c_outcomes(page: Page):
    special_cases = {
        "Identifying security incidents": [outcome_page.choose_policy_requirement_met]
    }
    outcome_page.complete_outcomes(page, special_cases, has_next=True)
