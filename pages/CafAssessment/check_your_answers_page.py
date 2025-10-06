from playwright.sync_api import expect, Page
from helpers.playwright_helpers import to_be_visible


CHECKANSWERS_LOCATORS = {
    "heading": {"role": "heading", "name": "Check your answers", "level": 1},
    "outcomes": "#objectives-container tbody tr",
    "objective_a": {
        "role": "heading",
        "name": "Objective A: Managing risk",
        "level": 2,
    },
    "objective_b": {
        "role": "heading",
        "name": "Objective B: Protecting against cyber attack and data breaches",
        "level": 2,
    },
    "objective_c": {
        "role": "heading",
        "name": "Objective C: Detecting cyber security events",
        "level": 2,
    },
    "objective_d": {
        "role": "heading",
        "name": "Objective D: Minimising the impact of incidents",
        "level": 2,
    },
    "objective_e": {
        "role": "heading",
        "name": "Objective E: Using and sharing information appropriately",
        "level": 2,
    },
    "page_title": {"role": "heading", "name": "Check your answers", "level": 1},
}


def verify_check_your_answers_page_heading(page: Page):
    to_be_visible(page, **CHECKANSWERS_LOCATORS["heading"])


def verify_objective_section_title(page: Page):
    """Validate outcomes table shows correct objective titles"""
    to_be_visible(page, **CHECKANSWERS_LOCATORS["objective_a"])
    to_be_visible(page, **CHECKANSWERS_LOCATORS["objective_b"])
    to_be_visible(page, **CHECKANSWERS_LOCATORS["objective_c"])
    to_be_visible(page, **CHECKANSWERS_LOCATORS["objective_d"])
    to_be_visible(page, **CHECKANSWERS_LOCATORS["objective_e"])


def verify_outcomes_for_objectives(page: Page):
    """Validate outcomes table shows correct expectations, and user responses."""
    outcomes = page.locator("#objectives-container tbody tr")
    for value in range(outcomes.count()):
        each_outcome = outcomes.nth(value)
        outcome_title = each_outcome.locator("td").nth(0).inner_text()
        expected = each_outcome.locator("td").nth(1).inner_text()
        user_response = each_outcome.locator("td").nth(2).inner_text()
        try:
            expect(each_outcome.locator("td").nth(1)).to_have_text(user_response)
        except AssertionError:
            print(
                f" Principle {outcome_title}: Expected '{expected}' but found '{user_response}'"
            )
            raise


def verify_standards_met_status(page: Page):
    check_your_answers_status = (
        page.locator(".table.align-middle.mb-5.mt-3").nth(0).locator("td").nth(2)
    )
    expect(check_your_answers_status).to_have_text("Standards met")
