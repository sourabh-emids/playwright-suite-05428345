@issue_0020
Feature: Three capability groups visibility and content

  As a user, I want to see the three capability groups (AI, Engineering, Platforms)
  so that I understand emids capabilities.

  Background:
    Given I navigate to the homepage

  Scenario: Three capability groups are displayed
    When I view the Capabilities section
    Then the section heading should be "Capabilities that deliver on ambitious goals"
    And the AI capability group should be visible
    And the Engineering capability group should be visible
    And the Platforms capability group should be visible
