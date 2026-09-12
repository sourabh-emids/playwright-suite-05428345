"""Feature file for Issue 0037 - Google Tag Manager consent governance."""
Feature: Google Tag Manager consent governance

  Scenario: Core page works if GTM fails
    Given Google Tag Manager fails to load
    When The page loads
    Then Core page functionality is unaffected

  Scenario: Non-essential tags respect consent
    Given Non-essential tags are configured in GTM
    When Consent has not been granted
    Then Non-essential tags do not run before required consent

  Scenario: GTM does not block rendering
    Given A user loads the page
    When GTM script loads
    Then GTM loads non-blocking (async/deferred) and does not delay rendering

  Scenario: Ad blocker handling
    Given An ad blocker prevents GTM from loading
    When The page loads
    Then Core page functionality remains unaffected

  Scenario: CSP block handling
    Given Content Security Policy blocks GTM
    When The page loads
    Then Core page renders; GTM failure is handled gracefully

  Scenario: GTM timeout handling
    Given GTM script times out
    When The page loads
    Then Core content renders without waiting indefinitely for GTM
