from playwright.sync_api import Page
from helpers.playwright_helpers import to_be_visible, click


BEFOREYOUSTART_LOCATORS = {
    "heading": {"role": "heading", "level": 2, "name": "Before you start"},
    "start_now": {"role": "link", "name": "Start now"},
}


def verify_before_you_start_heading(page: Page):
    to_be_visible(page, **BEFOREYOUSTART_LOCATORS["heading"])


def click_start_now_button(page: Page):
    click(page, **BEFOREYOUSTART_LOCATORS["start_now"])
