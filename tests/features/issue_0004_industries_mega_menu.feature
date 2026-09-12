@issue_0004
Feature: Industries mega-menu content and navigation

  As a user, I want to access the Industries mega-menu
  so that I can explore industries served by emids.

  Background:
    Given I navigate to the homepage

  Scenario: Industries mega-menu displays industry options
    When I click the Industries navigation item
    Then the Industries mega-menu should appear
    And the menu should display Consumer industry option
    And the industry description should be visible
