"""Feature file for Issue 0023 - Platforms capability content rendering."""
Feature: Platforms capability content rendering

  Scenario: Platforms content renders correctly
    Given A user views the Capabilities section
    When The Platforms capability panel/card loads
    Then Platforms content renders as a card/panel matching the capability visual system

  Scenario: Platforms labels consistent with navigation
    Given A user compares Platforms label in section to header navigation
    When Labels are compared
    Then Labels use approved taxonomy consistently

  Scenario: Navigation and body naming consistency
    Given A user examines the Platforms section and header
    When Both are compared
    Then No inconsistent synonyms exist unless intentionally approved by content governance

  Scenario: Stale CMS content detection
    Given CMS content has been updated to a different taxonomy
    When The page renders
    Then QA/content validation detects naming mismatches in publishing workflow
