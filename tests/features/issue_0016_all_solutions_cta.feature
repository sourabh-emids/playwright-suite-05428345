@issue_0016
Feature: All Solutions CTA visibility and routing

  As a user, I want to click the All Solutions CTA and be routed to the solutions page
  so that I can explore all solutions.

  Background:
    Given I navigate to the homepage

  Scenario: All Solutions CTA is visible and routes correctly
    When I view the Featured Solutions section
    Then the "All solutions" CTA should be visible
    And the CTA should link to the solutions page

  Scenario: All Solutions CTA navigation works
    When I click the "All solutions" CTA
    Then I should be navigated to the solutions page
