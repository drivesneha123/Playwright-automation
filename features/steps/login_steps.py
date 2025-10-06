from behave import given, when
from behave.runner import Context

from pages import login_page


@given("a user has permission to view their organisation's CAF assessment")
def step_navigate(context: Context):
    login_page.navigate(context.page)


@when("the user successfully logs in")
@given("the user successfully logs in with username and password")
@given("the user successfully logs in")
def step_login(context: Context):
    creds = context.credentials
    username = creds["username"]
    password = creds["password"]
    login_page.login(context.page, username, password)
