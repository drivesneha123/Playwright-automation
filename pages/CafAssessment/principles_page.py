from playwright.sync_api import expect, Page
import json
from helpers.playwright_helpers import (
    click,
    to_be_visible,
    get_inner_text,
    expect_to_have_text,
)

"""Read data from a JSON file."""
with open("data/CAF_data.json", "r") as f:
    test_data = json.load(f)
    PRINCIPLE_COUNT = test_data["Principle_count"]
    PRINCIPLE_NAME = test_data["Principle_name"]
    PRINCIPLE_DESC = test_data["Principle_description"]
    OUTCOME_DETAILS = test_data["Outcome"]


PRINCIPLE_LOCATORS = {
    "principle_page_title": {"role": "heading", "level": 1, "index": 0},
    "back_to_objectives": {"role": "link", "name": "Back to objectives"},
    "next_objective": ".nhsuk-pagination-item--next span.nhsuk-pagination__page",
    "previous_objective": ".nhsuk-pagination-item--previous span.nhsuk-pagination__page",
    "outcome_title": ".caf-outcome-title",
}


def verify_principles_page_title(page: Page, objective_key):
    objective_name = f"Objective {objective_key.upper()}"
    to_be_visible(
        page, **PRINCIPLE_LOCATORS["principle_page_title"], name=objective_name
    )


def verify_all_outcome_title(page: Page, principle):
    """
    Verify all outcome titles for a given principle against JSON data.

    Iterates over OUTCOME_DETAILS keys that match the principle (excluding descriptions)
    and asserts that each title is visible and matches the expected text.

    :param page: Playwright Page instance
    :param principle: Principle key (e.g., "A1", "B2") used to filter outcomes
    """
    index = 0
    for key, expected_text in OUTCOME_DETAILS.items():
        # Only check titles belonging to the given principle (skip descriptions)
        if key.startswith(principle) and not key.endswith("_description"):
            to_be_visible(
                page, locator=PRINCIPLE_LOCATORS["outcome_title"], index=index
            )
            expect_to_have_text(
                page,
                locator=PRINCIPLE_LOCATORS["outcome_title"],
                index=index,
                expected_text=expected_text,
            )
            index += 1


def select_outcome(page: Page, outcome: str):
    if outcome in OUTCOME_DETAILS:
        click(page, text=OUTCOME_DETAILS[outcome])


def get_principle_config(objective: str):
    """
    Load principle config for a given objective (A-E)
    from JSON, including names, descriptions, and count.
    """
    return {
        "objective_key": objective,
        "principle_first": PRINCIPLE_NAME[f"{objective}1"],
        "principle_last": PRINCIPLE_NAME[f"{objective}{PRINCIPLE_COUNT[objective]}"],
        "principle_count": PRINCIPLE_COUNT[objective],
        "principle_first_desc": PRINCIPLE_DESC[f"{objective}1"],
        "principle_last_desc": PRINCIPLE_DESC[
            f"{objective}{PRINCIPLE_COUNT[objective]}"
        ],
    }


def verify_objective_principles_details(page: Page, objective):
    """
    Verify principle count, titles, and descriptions
    for the given objective against JSON config.
    """
    config = get_principle_config(objective)
    if not config:
        raise ValueError(f"No configuration found for outcome: {objective}")
    objectives_principle = page.get_by_role("region", name="Principles").get_by_role(
        "heading", level=2
    )
    principles_description = page.get_by_role("region", name="Principles").locator(
        "p.caf-item.readable"
    )
    expect(objectives_principle).to_have_count(config["principle_count"])
    expect(objectives_principle.nth(0)).to_have_text(config["principle_first"])
    expect(objectives_principle.nth(-1)).to_have_text(config["principle_last"])
    expect(principles_description.nth(0)).to_have_text(config["principle_first_desc"])
    expect(principles_description.nth(-1)).to_have_text(config["principle_last_desc"])


def click_back_to_objectives(page: Page):
    click(page, **PRINCIPLE_LOCATORS["back_to_objectives"])


def click_pagination(page: Page, pagination_action):
    if pagination_action == "Next":
        expected_objective_title = get_inner_text(
            page, locator=PRINCIPLE_LOCATORS["next_objective"]
        )
    elif pagination_action == "Previous":
        expected_objective_title = get_inner_text(
            page, locator=PRINCIPLE_LOCATORS["previous_objective"]
        )
    else:
        raise ValueError(f"Unsupported pagination action: {pagination_action}")
    click(page, role="link", name=pagination_action)
    objective_heading = page.locator("#heroChildContent").get_by_role(
        "heading", level=2
    )
    current_objective_title = objective_heading.inner_text()
    assert (
        current_objective_title in expected_objective_title
    ), f"Expected '{current_objective_title}' in '{expected_objective_title}'"
