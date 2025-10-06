from pages.CafAssessment import outcome_page
from playwright.sync_api import Page


def complete_objective_e_outcomes(page: Page):
    outcome_page.complete_outcomes(page, special_cases=None, has_next=False)
