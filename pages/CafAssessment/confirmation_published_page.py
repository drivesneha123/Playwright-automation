from playwright.sync_api import Page
from helpers.playwright_helpers import to_be_visible, expect_to_have_text

PUBLISHED_LOCATORS = {
    "confirmation_heading": {
        "role": "heading",
        "name": "Assessment published",
        "level": 1,
    },
    "confirmation_message": {"locator": "#confirmation-description"},
}


def verify_assessment_published_title(page: Page):
    to_be_visible(page, **PUBLISHED_LOCATORS["confirmation_heading"])


def verify_confirmation_sent_emailid(page: Page, username):
    expect_to_have_text(
        page,
        **PUBLISHED_LOCATORS["confirmation_message"],
        expected_text="Confirmation has been sent to " + username,
    )
