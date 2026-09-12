"""Feature file for Issue 0041 - LinkedIn marketing tags conditional integration."""
Feature: LinkedIn marketing tags conditional integration

  Scenario: LinkedIn tag respects consent
    Given User has not granted marketing consent
    When Page loads
    Then LinkedIn marketing/insight tags do not execute

  Scenario: Core page independent of LinkedIn
    Given LinkedIn tag fails to load
    When User navigates the page
    Then Core page remains independent and fully functional

  Scenario: Marketing consent required for LinkedIn
    Given User grants marketing consent
    When Page loads
    Then LinkedIn tag may execute with valid consent

  Scenario: Ad blocker handling
    Given An ad blocker prevents LinkedIn tag from loading
    When Page loads
    Then Core page remains unaffected
