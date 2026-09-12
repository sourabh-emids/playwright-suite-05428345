@issue_0006
Feature: Company navigation group keyboard and touch access

  As a user, I want to access the Company navigation group
  so that I can learn about emids.

  Background:
    Given I navigate to the homepage

  Scenario: Company mega-menu displays sections
    When I click the Company navigation item
    Then the Company mega-menu should appear
    And the menu should display "About Us" section
    And the menu should display "Connect with Us" section
