from behave import given, then, when
from behave.runner import Context

from pages import organisation_select_page, publications_page
from pages.CafAssessment import (
    before_you_start_page,
    check_your_answers_page,
    confirmation_published_page,
    objective_a_principles,
    objective_b_principles,
    objective_c_principles,
    objective_d_principles,
    objective_e_principles,
    objectives_page,
    outcome_page,
    principles_page,
    publish_assessment,
)


@then('the user must navigate to "Select organisation" page')
def verify_select_organisation_account_page_display(context: Context):
    organisation_select_page.verify_organisation_select_page_heading(context.page)


@when('the user chooses the "CAF" organisation as an Administrator')
@given('the user chooses the "CAF" organisation as an Administrator')
def select_caf_organisation(context: Context):
    creds = context.credentials
    organisation = creds["organisation"]
    organisation_select_page.select_caf_organisation(context.page, organisation)


@then("the CAF assessment landing page must be displayed")
@given("the user is on the CAF assessment landing page")
def verify_caf_landing_page_display(context: Context):
    objectives_page.verify_caf_landing_page_title(context.page)


@then("the page must display the essential functions section")
def verify_essential_function_display(context: Context):
    objectives_page.verify_essential_function_heading(context.page)


@then("a summary card for each objective must be displayed")
def verify_caf_objective_cards_display(context: Context):
    objectives_page.verify_objectives_title(context.page)


@when('the user selects "{objective}" objective')
def select_objective_card_on_objectives_page(context: Context, objective):
    objectives_page.select_objective(context.page, objective)


@then('the principles page associated with "{objective}" objective must be displayed')
@then('the principles page for the "{objective}" objective must be displayed')
@given('the user is viewing principles under an objective "{objective}"')
@given('the user is on Objective "{objective}" Principles page')
def verify_principles_page_display(context: Context, objective):
    principles_page.verify_principles_page_title(context.page, objective)


@then(
    'each principle of "{objective}" objective must include an identifier, title, and description'
)
def verify_on_principles_page(context: Context, objective):
    principles_page.verify_objective_principles_details(context.page, objective)


@when('the user selects "{pagination}"')
def click_pagination(context: Context, pagination):
    principles_page.click_pagination(context.page, pagination)


@given('the user is viewing outcomes under a principle "{principle}"')
def verify_outcome_titles_on_principles_page(context: Context, principle):
    principles_page.verify_all_outcome_title(context.page, principle)


@when('the user selects an outcome "{outcome}"')
def select_outcome(context: Context, outcome):
    principles_page.select_outcome(context.page, outcome)


@given('the user is on the Outcome page "{outcome}"')
def verify_outcome_page_display(context: Context, outcome):
    outcome_page.verify_outcome_page_title(context.page, outcome)


@then('the "{outcome}" outcome page must display all outcome details')
def verify_on_outcome_page(context: Context, outcome):
    outcome_page.verify_outcome_page_details(context.page, outcome)


@when('the user selects Back to objective "{objective}"')
def click_back_to_objective(context: Context, objective):
    outcome_page.click_back_to_objective(context.page, objective)


@then("the user must be able to fill out all outcomes for all objective")
def fill_out_all_objective_outcomes(context: Context):
    objective_a_principles.complete_objective_a_outcomes(context.page)
    objective_b_principles.complete_objective_b_outcomes(context.page)
    objective_c_principles.complete_objective_c_outcomes(context.page)
    objective_d_principles.complete_objective_d_outcomes(context.page)
    objective_e_principles.complete_objective_e_outcomes(context.page)


@when('the user selects "Back to objectives" link')
def click_back_to_objectives(context: Context):
    principles_page.click_back_to_objectives(context.page)


@given("the user is on Objectives page")
@then('the user must navigate to "Objectives" page')
def verify_objectives_page_display(context: Context):
    objectives_page.verify_objectives_page_heading(context.page)


@when('the user chooses to "Publish Assessment" on Objectives page')
@when(
    "the user chooses to publish the CAF assessment after agreeing to the declaration"
)
def click_publish_assessment_button(context: Context):
    publish_assessment.click_publish_assessment_button(context.page)


@then('the user must navigate to the "Publish, before you start" page')
@given('the user is on "Publish, before you start" page')
def verify_on_before_you_start_page(context: Context):
    publish_assessment.verify_publish_assessment_heading(context.page)
    before_you_start_page.verify_before_you_start_heading(context.page)


@when('the user chooses to "Start now"')
def click_start_now_button(context: Context):
    before_you_start_page.click_start_now_button(context.page)


@then(
    'the user must navigate to the "Publish, Check your answers" page for their assessment'
)
@given('the user is on "Check your answers" page')
def verify_check_your_answers_page_display(context: Context):
    check_your_answers_page.verify_check_your_answers_page_heading(context.page)


@then('the user must see the status of publication as "Standards met"')
def verify_standards_met_status(context: Context):
    check_your_answers_page.verify_standards_met_status(context.page)


@then("the user must see a section for each objective")
def verify_objective_section(context: Context):
    """verify a section is displayed for each objective on the 'Check your answers' page"""
    check_your_answers_page.verify_objective_section_title(context.page)


@then(
    "each Outcome shows the expected level for standards met and what the outcome is currently set to"
)
def verify_outcomes_for_objectives(context: Context):
    check_your_answers_page.verify_outcomes_for_objectives(context.page)


@when('the user choose to "Continue" after reviewing assessment answers')
def click_continue_button(context: Context):
    """click 'Continue' button on Check your answers page"""
    publish_assessment.click_continue_button(context.page)


@then('the user must navigate to the "Publish your assessment, declaration" page')
@given('the user is on "Publish your assessment, declaration" page')
def verify_publish_assessment_confirmation_page_display(context: Context):
    publish_assessment.verify_publish_assessment_confirmation(context.page)


@then("the user must see a declaration statement for the CAF publication")
def verify_agreement_chekbox_display(context: Context):
    """verify 'I understand and agree with the above statements' checkbox"""
    publish_assessment.verify_agreement_chekbox(context.page)


@when(
    'the user agrees to the declaration "I understand and agree with the above statements"'
)
def click_agreement_checkbox(context: Context):
    publish_assessment.click_agreement_checkbox(context.page)


@then('the user must navigate to the "Assessment published" confirmation page')
@given('the user is on "Assessment published" confirmation page')
def verify_assessment_published_page_display(context: Context):
    confirmation_published_page.verify_assessment_published_title(context.page)


@then("the user's email id must be present in confirmation message")
def verify_confirmation_sent_emailid(context: Context):
    creds = context.credentials
    username = creds["username"]
    confirmation_published_page.verify_confirmation_sent_emailid(context.page, username)


@then('the user must see "View your published assessment" button')
def verify_published_assessment_button_display(context: Context):
    publish_assessment.verify_published_assessment_button(context.page)


@when('the user chooses to "View your published assessment"')
def click_view_published_assessment_button(context: Context):
    publish_assessment.click_view_published_assessment_button(context.page)


@then("the user must navigate to the list of previously published assessments")
def verify_publications_page_display(context: Context):
    publications_page.verify_publications_page_heading(context.page)


@then("the user must see currently published assessment with publication date")
def verify_currently_published_assessment(context: Context):
    publications_page.verify_currently_published_assessment(context.page)
