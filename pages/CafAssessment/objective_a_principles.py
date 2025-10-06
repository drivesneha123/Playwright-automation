from playwright.sync_api import Page
from pages.CafAssessment import outcome_page
from helpers.playwright_helpers import (
    fill_input,
)

OBJECTIVEA_LOCATORS = {
    "risk1": {"role": "textbox", "name": "Enter your top priority risk"},
    "risk2": {"role": "textbox", "name": "Enter your second priority risk"},
    "risk3": {"role": "textbox", "name": "Enter your third priority risk"},
}


def complete_objective_a_outcomes(page: Page):
    special_cases_A = {
        "Risk management process": [enter_outcome_a2a_risk],
        "Assurance": [outcome_page.choose_policy_requirement_met],
    }
    outcome_page.complete_outcomes(page, special_cases=special_cases_A, has_next=True)


def enter_outcome_a2a_risk(page: Page):
    fill_input(page, **OBJECTIVEA_LOCATORS["risk1"], value="Automation risk1")
    fill_input(page, **OBJECTIVEA_LOCATORS["risk2"], value="Automation risk2")
    fill_input(page, **OBJECTIVEA_LOCATORS["risk3"], value="Automation risk3")
