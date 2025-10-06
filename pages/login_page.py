from dotenv import load_dotenv
from playwright.sync_api import Page
from helpers.playwright_helpers import click, fill_input
import os

load_dotenv()
base_url = os.getenv("BASE_URL")

LOGIN_LOCATORS = {
    "log_in_link": {"text": "Log in"},
    "email_address": {"label": "Email Address"},
    "password": {"label": "Password"},
    "login_button": {"role": "button", "name": "Log in"},
}


def navigate(page: Page):
    page.goto(base_url)
    click(page, **LOGIN_LOCATORS["log_in_link"])


def login(page: Page, username, password):
    fill_input(page, **LOGIN_LOCATORS["email_address"], value=username)
    fill_input(page, **LOGIN_LOCATORS["password"], value=password)
    click(page, **LOGIN_LOCATORS["login_button"])
