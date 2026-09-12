@issue_0039
Feature: Campaign attribution parameters handling

  As a user, I want campaign attribution parameters to be preserved
  so that marketing can track traffic sources.

  Background:
    Given I navigate to the homepage with UTM parameters

  Scenario: UTM parameters are preserved in the session
    When I have UTM parameters in the URL
    Then the UTM parameters should be stored
    And the parameters should be available for analytics
