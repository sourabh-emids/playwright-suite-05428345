@issue_0002
Feature: Solutions mega-menu functionality and accessibility

  As a user, I want to access the Solutions mega-menu
  so that I can navigate to specific solution categories.

  Background:
    Given I navigate to the homepage

  Scenario: Solutions mega-menu opens and displays categories
    When I click the Solutions navigation item
    Then the Solutions mega-menu should appear
    And the menu should display "Solutions by Initiative"
    And the menu should display "Modernization" solution
    And the menu should display "Interoperability" solution
    And the menu should display "Cloud Transformation" solution
    And the menu should display "Agentic AI" solution
    And the menu should display "Global Capability Center" solution
    And the menu should display "Browse By Industry" section
    And the menu should display "Payers" industry
    And the menu should display "Providers" industry
    And the menu should display "Health Tech" industry
    And the menu should display "Life Sciences" industry
    And the menu should display "The Portfolio" section

  Scenario: Solutions mega-menu links are accessible
    When I click the Solutions navigation item
    Then each solution link should be clickable
    And each industry link should be clickable
    And the "Explore all solutions" link should be present

  Scenario: Solutions mega-menu closes on navigation
    When I click the Solutions navigation item
    And I click the "Modernization" solution link
    Then the mega-menu should close
    And I should be navigated to the Modernization page
