@issue_0007
Feature: Header Connect CTA visibility and routing

  As a user, I want to access the Contact page via the Connect CTA
  so that I can get in touch with emids.

  Background:
    Given I navigate to the homepage

  Scenario: Header Connect CTA is visible and routes correctly
    When I view the header
    Then the Connect CTA should be visible
    And the Connect CTA should link to the contact page

  Scenario: Connect CTA navigation works
    When I click the Connect CTA in the header
    Then I should be navigated to the contact page
