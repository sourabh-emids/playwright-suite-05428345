"""Feature file for Issue 0034 - Final conversion banner rendering."""
Feature: Final conversion banner rendering

  Scenario: Banner appears before footer
    Given A user scrolls to the bottom of the page
    When The user reaches the end of main content
    Then The final conversion banner appears before the footer

  Scenario: Primary action clear and keyboard operable
    Given A user views the final conversion banner
    When The user examines or interacts with the CTA
    Then Primary action is clear and keyboard operable

  Scenario: Supporting content readable
    Given A user views the final conversion banner
    When The user examines the supporting copy
    Then Timing/message content is readable

  Scenario: Required message and CTA fields present
    Given A user examines the final CTA section
    When The content is analyzed
    Then Required message and CTA fields are present

  Scenario: High-contrast closing CTA section
    Given A user views the final conversion banner
    When The contrast is measured
    Then The section meets WCAG AA contrast requirements

  Scenario: CTA text wrapping handling
    Given A user views the final CTA at narrow viewport
    When The CTA text is long
    Then Text wraps gracefully without overlapping or breaking functionality

  Scenario: Contact route unavailable handling
    Given The contact page is unavailable
    When A user clicks the final CTA
    Then Appropriate error handling occurs
