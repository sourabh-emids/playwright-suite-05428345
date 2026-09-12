@issue_0024
Feature: Five audience entries rendering and Explore actions

  As a user, I want to see five audience entries with Explore actions
  so that I can find content relevant to my industry.

  Background:
    Given I navigate to the homepage

  Scenario: Five audience entries are displayed with Explore actions
    When I view the Who We Serve section
    Then five audience entries should be visible
    And the audience should include Payer
    And the audience should include Provider
    And the audience should include HealthTech
    And the audience should include Life Sciences
    And the audience should include Consumer
    And each audience should have an Explore action
