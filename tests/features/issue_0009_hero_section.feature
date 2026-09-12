@issue_0009
Feature: Hero section rendering and H1 uniqueness

  As a user, I want to see the hero section with proper heading structure
  so that I understand the main value proposition.

  Background:
    Given I navigate to the homepage

  Scenario: Hero section renders correctly with unique H1
    When I view the hero section
    Then the hero section should be visible
    And there should be exactly one H1 heading
    And the H1 should contain "In Healthcare, Only Outcomes Matter"
    And the subtitle should be present
