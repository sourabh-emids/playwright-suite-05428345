@issue_0026
Feature: Insights section six content cards rendering

  As a user, I want to see six content cards in the Insights section
  so that I can discover relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: Six content cards are displayed in Insights section
    When I view the Insights section
    Then the section heading should be "The intelligence behind the outcomes"
    And six content cards should be visible
