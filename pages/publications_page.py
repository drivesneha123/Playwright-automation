from datetime import datetime
from playwright.sync_api import Page
from helpers.playwright_helpers import to_be_visible, expect_to_contain_text

today_date = datetime.now().strftime("%d/%m/%Y")

PUBLICATIONS_LOCATORS = {
    "publications_table": {"locator": "#tblPublications"},
    "publications_page_heading": {
        "text": "A list of previous publications is available on this page. You can select a publication to view further details."
    },
    "published_date": {
        "locator": "td.hidden-xs.publish-content",
        "index": 0,
    },
}


def verify_publications_page_heading(page: Page):
    to_be_visible(page, **PUBLICATIONS_LOCATORS["publications_table"])
    to_be_visible(page, **PUBLICATIONS_LOCATORS["publications_page_heading"])


def verify_currently_published_assessment(page: Page):
    """verify published assessment present under Publication list with today's date"""
    expect_to_contain_text(
        page, **PUBLICATIONS_LOCATORS["published_date"], expected_text=today_date
    )
