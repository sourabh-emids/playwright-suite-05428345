@issue_0010
Feature: Hero CTA routing to FDCE experience

  As a user, I want to click the Hero CTA and be routed to the FDCE experience
  so that I can learn more about how emids delivers outcomes.

  Background:
    Given I navigate to the homepage

  Scenario: Hero CTA routes to FDCE page
    When I view the hero section
    Then the "See How We Deliver Outcomes" CTA should be visible
    And the CTA should link to the FDCE page

  Scenario: Hero CTA navigation works
    When I click the "See How We Deliver Outcomes" CTA
    Then I should be navigated to the FDCE page
