from playwright.sync_api import Page
from helpers.playwright_helpers import to_be_visible, click


PUBLISH_ASSESSMENT_LOCATORS = {
    "publish_assessment_button": {"role": "button", "name": "Publish assessment"},
    "publish_assessment_heading": {
        "role": "heading",
        "name": "Publish your assessment",
    },
    "continue_button": {"role": "link", "name": "Continue"},
    "user_understands_and_agrees_checkbox": "I understand and agree with the above statements",
    "view_published_assessment_button": {
        "role": "link",
        "name": "View your published assessments",
    },
}


def click_publish_assessment_button(page: Page):
    click(page, **PUBLISH_ASSESSMENT_LOCATORS["publish_assessment_button"])


def verify_publish_assessment_heading(page: Page):
    to_be_visible(page, **PUBLISH_ASSESSMENT_LOCATORS["publish_assessment_heading"])


def click_continue_button(page: Page):
    click(page, **PUBLISH_ASSESSMENT_LOCATORS["continue_button"])


def verify_publish_assessment_confirmation(page: Page):
    to_be_visible(page, **PUBLISH_ASSESSMENT_LOCATORS["publish_assessment_heading"])


def verify_agreement_chekbox(page: Page):
    to_be_visible(
        page, label=PUBLISH_ASSESSMENT_LOCATORS["user_understands_and_agrees_checkbox"]
    )


def click_agreement_checkbox(page: Page):
    click(
        page, label=PUBLISH_ASSESSMENT_LOCATORS["user_understands_and_agrees_checkbox"]
    )


def verify_published_assessment_button(page: Page):
    to_be_visible(
        page, **PUBLISH_ASSESSMENT_LOCATORS["view_published_assessment_button"]
    )


def click_view_published_assessment_button(page: Page):
    click(page, **PUBLISH_ASSESSMENT_LOCATORS["view_published_assessment_button"])
