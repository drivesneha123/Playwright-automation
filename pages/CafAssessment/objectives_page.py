from playwright.sync_api import Page
from helpers.playwright_helpers import (
    click,
    to_be_visible,
    expect_to_contain_text,
)


OBJECTIVES_LOCATORS = {
    "page_title": {"locator": "#pagetitle"},
    "objective_title": {"role": "heading", "name": "Objectives", "level": 2},
    "objective_a_name": {"role": "link", "name": "A. Managing risk"},
    "objective_b_name": {
        "role": "link",
        "name": "B. Protecting against cyber attack and data breaches",
    },
    "objective_c_name": {"role": "link", "name": "C. Detecting cyber security events"},
    "objective_d_name": {
        "role": "link",
        "name": "D. Minimising the impact of incidents",
    },
    "objective_e_name": {
        "role": "link",
        "name": "E. Using and sharing information appropriately",
    },
    "publish_assessment_heading": {
        "role": "heading",
        "name": "Publish your assessment",
        "level": 2,
    },
    "essentital_functions": {
        "role": "heading",
        "level": 2,
        "name": "Essential Functions",
    },
    "progress_bar": {"role": "heading", "level": 2, "name": "Progress"},
}


def verify_caf_landing_page_title(page: Page):
    expect_to_contain_text(
        page,
        **OBJECTIVES_LOCATORS["page_title"],
        expected_text="Complete your assessment",
    )
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_title"])


def verify_objectives_title(page: Page):
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_a_name"])
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_b_name"])
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_c_name"])
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_d_name"])
    to_be_visible(page, **OBJECTIVES_LOCATORS["objective_e_name"])


def select_objective(page: Page, objective_key):
    mapping = {
        "A": "objective_a_name",
        "B": "objective_b_name",
        "C": "objective_c_name",
        "D": "objective_d_name",
        "E": "objective_e_name",
    }

    objective_name = mapping.get(objective_key)
    if not objective_name:
        raise ValueError(f"Invalid objective name: {objective_key}")

    click(page, **OBJECTIVES_LOCATORS[objective_name])
    to_be_visible(page, **OBJECTIVES_LOCATORS["progress_bar"])


def verify_objectives_page_heading(page: Page):
    to_be_visible(page, **OBJECTIVES_LOCATORS["publish_assessment_heading"])


def verify_essential_function_heading(page: Page):
    to_be_visible(page, **OBJECTIVES_LOCATORS["essentital_functions"])
