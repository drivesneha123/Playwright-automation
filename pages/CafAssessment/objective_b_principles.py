from playwright.sync_api import expect, Page
from pages.CafAssessment import outcome_page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from helpers.playwright_helpers import to_be_visible, file_upload, fill_input, click


OBJECTIVE_B_LOCATOR = {
    "b4d_desktop_percentage": "#AdditionalDataPercentage\\~B4\\.d\\.dc1",
    "b4d_server_percentage": "#AdditionalDataPercentage\\~B4\\.d\\.dc2",
    "save_and_continue": {"role": "button", "name": "Save and continue"},
    "continue": {"role": "button", "name": "Continue"},
    "uploaded_evidence": "a#download-evidence-0",
    "mfa_upload_evidence_yes_radio": "Yes, with exceptions (you'll be asked to upload details of these)",
    "MFA_requirement_met": '//dt[@class="nhsuk-summary-list__key" and contains(text(), "Requirement met")]/following-sibling::*[1]',
    "MFA_policy_page": {
        "role": "heading",
        "level": 1,
        "name": "Mandatory policy requirement: multi-factor authentication",
    },
    "requirement_met_change_link": ".nhsuk-summary-list__actions",
}


def enter_b4d_supported_version_percentage(page: Page):
    fill_input(page, locator=OBJECTIVE_B_LOCATOR["b4d_desktop_percentage"], value="50")
    fill_input(page, locator=OBJECTIVE_B_LOCATOR["b4d_server_percentage"], value="60")


def upload_MFA_evidence(page: Page):
    click(page, label=OBJECTIVE_B_LOCATOR["mfa_upload_evidence_yes_radio"])
    click(page, **OBJECTIVE_B_LOCATOR["save_and_continue"])
    file_upload(page, "files/6001-kb.jpg")
    to_be_visible(page, locator=OBJECTIVE_B_LOCATOR["uploaded_evidence"])
    click(page, **OBJECTIVE_B_LOCATOR["continue"])


def principle_b2a_mfa_upload(page: Page):
    """
    Handle MFA (Multi-Factor Authentication) evidence upload for Outcome B2.a.

    This function covers two scenarios:
      1. User lands on the B2.a outcome page where the "Requirement met" value is saved as "No".
      2. User lands directly on the MFA policy evidence page.

    :param page: Playwright Page instance
    :raises PlaywrightTimeoutError: If the MFA policy page is not visible within the timeout.
    """
    # Case 1: Requirement met = "No", so user clicks 'Change' to upload MFA
    MFA_policy_page = page.get_by_role(**OBJECTIVE_B_LOCATOR["MFA_policy_page"])
    mfa_upload_evidence_yes_radio = page.get_by_label(
        OBJECTIVE_B_LOCATOR["mfa_upload_evidence_yes_radio"]
    )
    MFA_requirement_met = page.locator(OBJECTIVE_B_LOCATOR["MFA_requirement_met"])
    if (
        MFA_requirement_met.is_visible()
        and MFA_requirement_met.inner_text() != "Yes, with exceptions"
    ):
        page.locator(OBJECTIVE_B_LOCATOR["requirement_met_change_link"]).locator(
            "a"
        ).click()
        upload_MFA_evidence(page)
    # Case 2: User directly lands on MFA evidence page
    elif not MFA_requirement_met.is_visible():
        try:
            MFA_policy_page.wait_for(state="visible", timeout=100)
            if MFA_policy_page.is_visible():
                expect(mfa_upload_evidence_yes_radio).to_be_visible()
                upload_MFA_evidence(page)
        except PlaywrightTimeoutError:
            print("MFA page not visible..")


def complete_objective_b_outcomes(page: Page):
    special_cases = {
        "Identity verification, authentication and authorisation": [
            principle_b2a_mfa_upload
        ],
        "Vulnerability management": [
            outcome_page.choose_policy_requirement_met,
            enter_b4d_supported_version_percentage,
        ],
    }
    outcome_page.complete_outcomes(page, special_cases=special_cases, has_next=True)
