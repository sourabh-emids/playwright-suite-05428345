Feature: Footer legal navigation rendering

  Scenario: Each legal link has descriptive text
    Given User views footer legal navigation
    When Page renders
    Then Each legal link has descriptive text (Privacy Policy, Cookie Policy, Accessibility Statement, etc.)

  Scenario: Each legal link has valid destination
    Given User inspects footer legal links
    When Links render
    Then Each link has a valid HTTPS destination

  Scenario: Each legal link has visible focus state
    Given User tabs to footer legal links
    When Focus is received
    Then Visible focus state is displayed

  Scenario: Labels not blank
    Given Footer legal links render
    When User validates content
    Then No labels are blank

  Scenario: All URLs HTTPS
    Given Footer legal links render
    When User inspects URLs
    Then All URLs use HTTPS protocol

  Scenario: Legal page moved handling
    Given Legal page URL has changed
    When User clicks link
    Then User is redirected to current location or sees appropriate error

  Scenario: Long labels handled
    Given Legal link has long label
    When Page renders at mobile width
    Then Label wraps appropriately

  Scenario: Locale variant handling
    Given Site has multiple locales
    When User views footer
    Then Legal links are available for current locale or default
