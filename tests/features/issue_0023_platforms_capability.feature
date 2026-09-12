@issue_0023
Feature: Platforms capability taxonomy consistency

  As a user, I want to see Platforms capability with consistent taxonomy
  so that I can understand emids platform capabilities.

  Background:
    Given I navigate to the homepage

  Scenario: Platforms capability displays with consistent taxonomy
    When I view the Capabilities section
    Then the Platforms capability section should be visible
    And the Platforms section should have consistent naming
