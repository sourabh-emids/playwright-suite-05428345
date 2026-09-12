@issue_0055
Feature: Homepage modal behavior default state

  As a user, I want modals to have correct default state
  so that the page experience is as intended.

  Background:
    Given I navigate to the homepage

  Scenario: Modal has correct default state on page load
    When the page loads
    Then no modal should be visible by default
    And the main content should be accessible
