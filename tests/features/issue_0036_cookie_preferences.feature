@issue_0036
Feature: Cookie Preferences control visibility in footer

  As a user, I want to access cookie preferences
  so that I can manage my privacy settings.

  Background:
    Given I navigate to the homepage

  Scenario: Cookie preferences control is accessible
    When I view the footer
    Then the cookie settings button should be visible
    And clicking it should open cookie preferences
