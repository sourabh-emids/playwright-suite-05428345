@issue_0031
Feature: FinOps healthcare payer resource card display

  As a user, I want to see the FinOps healthcare payer resource card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: FinOps resource card is displayed
    When I view the Insights section
    Then the FinOps resource card should be visible
    And the card should have a Read More action
