@E2ERegression
@login_viewer
Feature: CAF Assessment Navigation and Display
As a user completing my organisation's CAF assessment
I want to navigate between objectives, principles, and outcomes
So that I can complete the assessment accurately.


Scenario: Redirect to CAF assessment on login
    Given a user has permission to view their organisation's CAF assessment
    When the user successfully logs in
    And the user chooses the "CAF" organisation as an Administrator
    Then the CAF assessment landing page must be displayed

Scenario: Display of objectives on landing page
    Given the user is on the CAF assessment landing page
    Then the page must display the essential functions section
    And a summary card for each objective must be displayed

Scenario:Viewing principles under an objective
    Given the user is on the CAF assessment landing page
    When the user selects "B" objective
    Then the principles page associated with "B" objective must be displayed
    And each principle of "B" objective must include an identifier, title, and description

Scenario: Navigate to the next objective
    Given the user is viewing principles under an objective "B"
    When the user selects "Next"
    Then the principles page for the "C" objective must be displayed

Scenario: Navigate to the previous objective
    Given the user is viewing principles under an objective "C"
    When the user selects "Previous"
    Then the principles page for the "B" objective must be displayed

Scenario: Viewing outcome-level details
    Given the user is viewing outcomes under a principle "B1"
    When the user selects an outcome "B1.a"
    Then the "B1.a" outcome page must display all outcome details

Scenario: Navigating back to principles from outcome page
    Given the user is on the Outcome page "B1.a"
    When the user selects Back to objective "B"
    Then the principles page associated with "B" objective must be displayed

Scenario: Navigating back to objectives from Principle page
    Given the user is on Objective "B" Principles page
    When the user selects "Back to objectives" link
    Then the CAF assessment landing page must be displayed
