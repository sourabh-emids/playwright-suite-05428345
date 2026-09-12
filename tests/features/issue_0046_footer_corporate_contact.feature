@issue_0046
Feature: Footer corporate contact information rendering

  As a user, I want to see corporate contact information in the footer
  so that I can reach emids through official channels.

  Background:
    Given I navigate to the homepage

  Scenario: Footer displays corporate contact information
    When I view the footer
    Then the footer logo should be visible
    And the footer Connect link should be present
