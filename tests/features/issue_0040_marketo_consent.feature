@issue_0040
Feature: Marketo marketing integration consent gating

  As a user, I want Marketo to only load after marketing consent
  so that my data is not shared without permission.

  Background:
    Given I navigate to the homepage

  Scenario: Marketo loads only after marketing consent
    When I have not given marketing consent
    Then Marketo should not be active
