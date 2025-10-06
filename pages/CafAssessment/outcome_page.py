from playwright.sync_api import Page
from pages.CafAssessment import principles_page
import json
from helpers.playwright_helpers import (
    click,
    get_inner_text,
    to_be_visible,
    fill_input,
    expect_to_have_text,
)

"""Read data from a JSON file."""
with open("data/CAF_data.json", "r") as f:
    test_data = json.load(f)
    OUTCOME_DETAILS = test_data["Outcome"]


OUTCOME_LOCATORS = {
    "outcome_expectation": ".caf-outcome-expectation",
    "outcome_title": {"role": "heading", "level": 2, "index": 0},
    "outcome_description": {"locator": ".preserve-whitespace", "index": 0},
    "mandatory_policy_heading": {
        "role": "heading",
        "level": 2,
        "index": 0,
        "name": "Mandatory policy requirement",
    },
    "policy_requirment_met": {"role": "radio", "name": "Yes"},
    "supporting_info": {"role": "textbox", "name": "Supporting Information"},
    "save_and_continue": {"role": "button", "name": "Save and continue"},
    "progress_bar": {"role": "progressbar", "name": "Assertions confirmed progress"},
    "save_as_complete": {"label": "Save as complete"},
    "expected_achievement_level": {"locator": ".caf-outcome-expectation"},
}


def choose_policy_requirement_met(page: Page):
    click(page, **OUTCOME_LOCATORS["policy_requirment_met"])


def complete_outcomes(
    page: Page,
    special_cases: dict[str, list[callable]] = None,
    has_next: bool = True,
):
    """
    Generic function to complete any objective.

    :param page: Playwright Page instance
    :param verify_principle_count: function to verify principle count for the objective
    :param special_cases: dict mapping outcome where policy requirement, risk data is present -> handler function
    :param has_next: whether this objective has a 'Next' pagination link
    """
    objectives_outcome = page.locator(".caf-outcome-title")
    total = objectives_outcome.count()
    for each_outcome in range(total):
        element = objectives_outcome.nth(each_outcome)
        outcome_title = element.inner_text()
        element.click()

        # Handle special cases if present
        if special_cases and outcome_title in special_cases:
            for handler in special_cases[outcome_title]:
                handler(page)

        # Common steps for all objectives
        select_expected_achievement_level(page)
        enter_supporting_info(page)
        mark_outcome_as_complete(page)
        save_outcome(page)
    if has_next:
        principles_page.click_pagination(page, "Next")


def select_expected_achievement_level(page: Page):
    to_be_visible(page, **OUTCOME_LOCATORS["expected_achievement_level"])
    expectations = get_inner_text(
        page, **OUTCOME_LOCATORS["expected_achievement_level"]
    )

    radio_button = page.locator("div.radio")
    for button in range(radio_button.count()):
        radio_button_text = radio_button.nth(button).locator("label")
        if radio_button_text.text_content().strip() == expectations:
            radio_button_text.click()
            break


def enter_supporting_info(page: Page):
    fill_input(page, **OUTCOME_LOCATORS["supporting_info"], value="Automation test")


def mark_outcome_as_complete(page: Page):
    click(page, **OUTCOME_LOCATORS["save_as_complete"])


def save_outcome(page: Page):
    """Save the current outcome and confirm navigation to the Principles page."""
    click(page, **OUTCOME_LOCATORS["save_and_continue"])
    to_be_visible(page, **OUTCOME_LOCATORS["progress_bar"])


OUTCOME_CONFIG = {
    "A1.a": {
        "title": OUTCOME_DETAILS["A1.a"],
        "description": OUTCOME_DETAILS["A1.a_description"],
        "achievement_levels": ["Not achieved", "Achieved"],
        "policy_requirement": False,
    },
    "A2.b": {
        "title": OUTCOME_DETAILS["A2.b"],
        "description": OUTCOME_DETAILS["A2.b_description"],
        "achievement_levels": ["Not achieved", "Achieved"],
        "policy_requirement": True,
    },
    "B1.a": {
        "title": OUTCOME_DETAILS["B1.a"],
        "description": OUTCOME_DETAILS["B1.a_description"],
        "achievement_levels": ["Not achieved", "Partially achieved", "Achieved"],
        "policy_requirement": False,
    },
}


def verify_outcome_page_details(page: Page, outcome: str):
    """
    Verify outcome page details including title, description,
    achievement levels, and mandatory policy requirement section.
    """
    config = OUTCOME_CONFIG.get(outcome)
    if not config:
        raise ValueError(f"No configuration found for outcome: {outcome}")

    # Outcome expectation
    to_be_visible(page, locator=OUTCOME_LOCATORS["outcome_expectation"])

    # Title and description
    expect_to_have_text(
        page,
        **OUTCOME_LOCATORS["outcome_title"],
        expected_text=config["title"],
    )
    expect_to_have_text(
        page,
        **OUTCOME_LOCATORS["outcome_description"],
        expected_text=config["description"],
    )

    # Achievement levels
    for level in config.get("achievement_levels", []):
        to_be_visible(page, role="radio", name=level)

    # Mandatory policy requirement
    if config.get("policy_requirement", True):
        to_be_visible(page, **OUTCOME_LOCATORS["mandatory_policy_heading"])


def verify_outcome_page_title(page: Page, outcome):
    config = OUTCOME_CONFIG.get(outcome)
    expect_to_have_text(
        page,
        **OUTCOME_LOCATORS["outcome_title"],
        expected_text=config["title"],
    )


def click_back_to_objective(page: Page, objective_key):
    click(page, role="link", name=f"Back to objective {objective_key}")
