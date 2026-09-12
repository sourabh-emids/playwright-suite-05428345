@issue_0029
Feature: Life Sciences transformation eBook card display

  As a user, I want to see the Life Sciences transformation eBook card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: Life Sciences eBook card is displayed
    When I view the Insights section
    Then the Life Sciences eBook card should be visible
