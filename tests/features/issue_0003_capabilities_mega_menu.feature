@issue_0003
Feature: Capabilities mega-menu accessibility and navigation

  As a user, I want to access the Capabilities mega-menu
  so that I can understand emids capabilities.

  Background:
    Given I navigate to the homepage

  Scenario: Capabilities mega-menu displays three capability groups
    When I click the Capabilities navigation item
    Then the Capabilities mega-menu should appear
    And the menu should display "AI" capability group
    And the menu should display "Engineering" capability group
    And the menu should display "Platforms" capability group

  Scenario: Capabilities mega-menu links are navigable
    When I click the Capabilities navigation item
    Then each capability link should be clickable
    And the capability descriptions should be present
