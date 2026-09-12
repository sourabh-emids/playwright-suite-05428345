@issue_0022
Feature: Engineering capability content rendering

  As a user, I want to see Engineering capability content
  so that I can learn about emids engineering capabilities.

  Background:
    Given I navigate to the homepage

  Scenario: Engineering capability content is rendered correctly
    When I view the Capabilities section
    Then the Engineering capability section should be visible
