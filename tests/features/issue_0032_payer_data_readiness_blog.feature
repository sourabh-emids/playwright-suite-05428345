@issue_0032
Feature: Payer data readiness blog card display

  As a user, I want to see the Payer data readiness blog card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: Payer data readiness blog card is displayed
    When I view the Insights section
    Then the Payer data readiness blog card should be visible
