@issue_0013
Feature: See the model CTA routing and operation

  As a user, I want to click the "See the model" CTA and be routed to the FDCE page
  so that I can learn more about the delivery model.

  Background:
    Given I navigate to the homepage

  Scenario: See the model CTA routes correctly
    When I view the How We Deliver section
    Then the "See the model" CTA should be visible
    And the CTA should link to the FDCE page

  Scenario: See the model CTA navigation works
    When I click the "See the model" CTA
    Then I should be navigated to the FDCE page
