@issue_0030
Feature: AI ROI eBook card display

  As a user, I want to see the AI ROI eBook card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: AI ROI eBook card is displayed
    When I view the Insights section
    Then the AI ROI eBook card should be visible
