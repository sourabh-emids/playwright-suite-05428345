@issue_0021
Feature: AI capability content rendering and links

  As a user, I want to see AI capability content with working links
  so that I can learn about emids AI capabilities.

  Background:
    Given I navigate to the homepage

  Scenario: AI capability content is rendered correctly
    When I view the Capabilities section
    Then the AI capability section should be visible
    And AI capability links should be present
