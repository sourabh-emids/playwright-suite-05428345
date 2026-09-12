"""Feature file for Issue 0031 - FinOps healthcare payer resource card."""
Feature: FinOps healthcare payer resource card

  Scenario: FinOps resource card renders correctly
    Given A user views the FinOps healthcare payer resource card
    When The card renders
    Then Card renders with title, type, action and routes correctly to configured destination

  Scenario: Valid destination required
    Given A user clicks the FinOps resource card action
    When The action is activated
    Then User is navigated to the valid destination

  Scenario: Broken link handling
    Given The FinOps resource link is broken
    When A user clicks the card
    Then Appropriate error handling or redirect occurs
