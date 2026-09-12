@issue_0041
Feature: LinkedIn marketing tags conditional loading

  As a user, I want LinkedIn tags to load only after consent
  so that my browsing is not tracked without permission.

  Background:
    Given I navigate to the homepage

  Scenario: LinkedIn tags load conditionally
    When I have not given marketing consent
    Then LinkedIn tags should not be active
