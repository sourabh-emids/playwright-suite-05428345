Feature: Footer legal navigation rendering

  Scenario: Each legal link has descriptive text
    Given Footer legal links
    When Links are inspected
    Then Each link has descriptive text (Privacy Policy, Cookie Policy, Accessibility Statement, etc.)

  Scenario: Legal links have valid destinations
    Given Footer legal link URLs
    When URLs are verified
    Then All URLs are HTTPS and published

  Scenario: Visible focus state on legal links
    Given Legal navigation links
    When Keyboard focus is tested
    Then Visible focus state is present

  Scenario: Labels not blank
    Given Legal link labels
    When Labels are verified
    Then Labels are populated (not blank)

  Scenario: Legal page moved handling
    Given Edge case where legal page is moved
    When Link is followed
    Then Appropriate redirect or error handling occurs
