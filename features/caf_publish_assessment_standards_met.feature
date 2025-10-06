@E2ERegression
@login_administrator
Feature: Complete and Publish the CAF Assessment
Ensure that a user can complete all CAF objectives and principles
and publish the assessment successfully.


  Scenario: User records outcomes for every objective
    Given a user has permission to view their organisation's CAF assessment
    When the user successfully logs in
    Then the user must navigate to "Select organisation" page
    When the user chooses the "CAF" organisation as an Administrator
    Then the CAF assessment landing page must be displayed
    And a summary card for each objective must be displayed
    When the user selects "A" objective
    Then the user must be able to fill out all outcomes for all objective
    When the user selects "Back to objectives" link
    Then the user must navigate to "Objectives" page

  Scenario: User initiates publishing from the Objectives page
    Given the user is on Objectives page
    When the user chooses to "Publish Assessment" on Objectives page
    Then the user must navigate to the "Publish, before you start" page

  Scenario: User reviews answers before publishing
    Given the user is on "Publish, before you start" page
    When the user chooses to "Start now"
    Then the user must navigate to the "Publish, Check your answers" page for their assessment
    And the user must see the status of publication as "Standards met"
    And the user must see a section for each objective
    And each Outcome shows the expected level for standards met and what the outcome is currently set to

  Scenario: User confirms agreement with the declaration before publishing a CAF assessment
    Given the user is on "Check your answers" page
    When the user choose to "Continue" after reviewing assessment answers
    Then the user must navigate to the "Publish your assessment, declaration" page
    And the user must see a declaration statement for the CAF publication

  Scenario: User publishes the assessment after agreeing to the declaration
    Given the user is on "Publish your assessment, declaration" page
    When the user agrees to the declaration "I understand and agree with the above statements"
    And the user chooses to publish the CAF assessment after agreeing to the declaration
    Then the user must navigate to the "Assessment published" confirmation page
    And the user's email id must be present in confirmation message

  Scenario: User views a published assessment
    Given the user is on "Assessment published" confirmation page
    When the user chooses to "View your published assessment"
    Then the user must navigate to the list of previously published assessments
    And the user must see currently published assessment with publication date
