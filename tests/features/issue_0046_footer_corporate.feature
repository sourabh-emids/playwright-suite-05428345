"""Feature file for Issue 0046 - Footer corporate/contact information rendering."""
Feature: Footer corporate/contact information rendering

  Scenario: Footer information readable at mobile widths
    Given A user views the footer on a mobile device
    When Footer content is rendered
    Then Corporate text and contact details remain readable

  Scenario: Footer does not conflict with legal navigation
    Given A user views the footer
    When All footer sections are visible
    Then Corporate information does not conflict with or overlap legal navigation

  Scenario: Only approved current content published
    Given A user examines footer content
    When Content is analyzed
    Then Only approved current corporate content is published

  Scenario: Outdated contact info detection
    Given Contact information has been updated in source systems
    When Footer renders
    Then Content governance detects outdated information before publishing

  Scenario: External social link unavailable handling
    Given A social link in the footer is unavailable
    When User clicks the social link
    Then Appropriate handling (broken link detected in monitoring)
