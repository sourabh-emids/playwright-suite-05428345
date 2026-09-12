@issue_0027
Feature: Medicare Advantage eBook card display

  As a user, I want to see the Medicare Advantage eBook card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: Medicare Advantage eBook card is displayed
    When I view the Insights section
    Then the Medicare Advantage eBook card should be visible
    And the card should have the eBook type indicator
    And the card should have a download action
