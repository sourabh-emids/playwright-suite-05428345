@issue_0025
Feature: Four impact proof metrics rendering

  As a user, I want to see four impact metrics
  so that I can understand emids track record.

  Background:
    Given I navigate to the homepage

  Scenario: Four impact metrics are displayed
    When I view the Impact section
    Then four metrics should be visible
    And each metric should have a number and label
