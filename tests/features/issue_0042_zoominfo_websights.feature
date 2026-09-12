@issue_0042
Feature: ZoomInfo WebSights conditional integration

  As a user, I want ZoomInfo WebSights to load only after consent
  so that my data is handled appropriately.

  Background:
    Given I navigate to the homepage

  Scenario: ZoomInfo WebSights loads conditionally
    When I have not given marketing consent
    Then ZoomInfo WebSights should not be active
