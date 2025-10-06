@login_viewer
Feature: CAF Assessment Navigation and Display
As a user completing my organisation's CAF assessment
I want to navigate between objectives, principles, and outcomes
So that I can complete the assessment accurately.

Background:
    Given a user has permission to view their organisation's CAF assessment
    And the user successfully logs in
    And the user chooses the "CAF" organisation as an Administrator
    And the user is on the CAF assessment landing page

Scenario: Display of objectives on landing page
    Then the page must display the essential functions section
    And a summary card for each objective must be displayed

Scenario: Viewing principles under an objective
    When the user selects "A" objective
    Then the principles page associated with "A" objective must be displayed
    And each principle of "A" objective must include an identifier, title, and description

Scenario Outline: Navigate between objective
    When the user selects "<objective>" objective
    And the user selects "<navigation>"
    Then the principles page for the "<adjacent>" objective must be displayed
    Examples:
    | objective | navigation | adjacent |
    | A         | Next       | B        |
    | B         | Previous   | A        |

Scenario: Viewing outcome-level details
    When the user selects "A" objective
    And the user selects an outcome "A1.a"
    Then the "A1.a" outcome page must display all outcome details

Scenario Outline: Navigating back to principles from outcome page
    When the user selects "<objective>" objective
    And the user selects an outcome "<outcome>"
    And the user selects Back to objective "<objective>"
    Then the principles page associated with "<objective>" objective must be displayed
    Examples:
    | objective | outcome |
    | A         | A1.a    |
    | A         | A2.b    |

Scenario Outline: Navigating back to objectives from Principle page
    When the user selects "<objective>" objective
    And the user selects "Back to objectives" link
    Then the CAF assessment landing page must be displayed
    Examples:
    | objective |
    |     A     |
    |     B     |
