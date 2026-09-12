@issue_0015
Feature: Six featured solutions rendering and numbering

  As a user, I want to see six featured solutions with proper numbering
  so that I can understand the solutions portfolio.

  Background:
    Given I navigate to the homepage

  Scenario: Six featured solutions are displayed
    When I view the Featured Solutions section
    Then six solution cards should be visible
    And each solution should have a number
    And each solution should have a title
    And each solution should have a description
