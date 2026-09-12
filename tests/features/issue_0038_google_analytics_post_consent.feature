@issue_0038
Feature: Google Analytics post-consent measurement

  As a user, I want Google Analytics to track after consent
  so that usage data is collected appropriately.

  Background:
    Given I navigate to the homepage

  Scenario: GA initializes after consent
    When I give analytics consent
    Then GA should be initialized
