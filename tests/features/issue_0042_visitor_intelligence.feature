"""Feature file for Issue 0042 - ZoomInfo/WebSights conditional integration."""
Feature: ZoomInfo/WebSights conditional integration

  Scenario: Tooling loads conditionally based on config and consent
    Given Visitor intelligence tool is not enabled or consent is not granted
    When Page loads
    Then Tooling does not load

  Scenario: Failure does not affect content or navigation
    Given Visitor intelligence tool fails to load
    When User navigates the page
    Then Content and navigation remain fully functional

  Scenario: No private account identifiers in page copy
    Given A user views the page source
    When The page HTML is examined
    Then Private account identifiers for visitor intelligence tools are not exposed in page copy

  Scenario: Consent denied handling
    Given User denies marketing/analytics consent
    When Page loads
    Then Visitor intelligence tooling does not load
