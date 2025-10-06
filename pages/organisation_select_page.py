from playwright.sync_api import Page
from helpers.playwright_helpers import to_be_visible, click


ORGSELECT_LOCATORS = {
    "organisation_select_page_heading": {
        "role": "heading",
        "name": "Select an Organisation",
        "level": 1,
    }
}


def verify_organisation_select_page_heading(page: Page):
    to_be_visible(page, **ORGSELECT_LOCATORS["organisation_select_page_heading"])


def select_caf_organisation(page: Page, organisation):
    click(page, locator=organisation)
