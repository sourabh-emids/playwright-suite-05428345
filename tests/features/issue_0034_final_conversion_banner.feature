@issue_0034
Feature: Final conversion banner rendering and CTA

  As a user, I want to see the final conversion banner with CTA
  so that I can take action to connect with emids.

  Background:
    Given I navigate to the homepage

  Scenario: Final conversion banner is rendered with CTA
    When I view the page
    Then the final CTA banner should be visible
    And the timing message should be visible
    And the Connect CTA should be present
