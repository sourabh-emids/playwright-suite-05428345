"""Feature file for Issue 0045 - Footer legal navigation rendering."""
Feature: Footer legal navigation rendering

  Scenario: Each legal link has descriptive text and valid destination
    Given A user views the footer legal navigation
    When Legal links are examined
    Then Each link has descriptive text, valid destination, and visible focus state

  Scenario: Legal links HTTPS and published
    Given A user examines footer legal link URLs
    When URLs are inspected
    Then All URLs are HTTPS and point to published pages

  Scenario: Labels not blank
    Given A user views footer legal links
    When Labels are examined
    Then Labels are not blank

  Scenario: Legal page moved handling
    Given A legal page has been moved without redirect
    When User clicks the footer legal link
    Then Broken link is detected in monitoring

  Scenario: Long labels handling
    Given A legal link label exceeds expected length
    When Footer renders at mobile width
    Then Label wraps gracefully without breaking layout
