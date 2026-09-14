Feature: Render footer legal navigation

  Scenario: Privacy Policy link present with valid destination
    Given User views footer
    When Locating Privacy Policy
    Then Privacy Policy link visible and routes to valid HTTPS destination

  Scenario: Cookie Policy link present with valid destination
    Given User views footer
    When Locating Cookie Policy
    Then Cookie Policy link visible and routes to valid HTTPS destination

  Scenario: Accessibility Statement link present
    Given User views footer
    When Locating Accessibility
    Then Accessibility Statement link visible with valid destination

  Scenario: Other approved legal links present
    Given Additional legal links configured
    When Checking footer
    Then Additional approved legal links display with descriptive text

  Scenario: Legal links have visible focus state
    Given User tabs to legal link
    When Checking focus
    Then Visible focus indicator present on legal links

  Scenario: Labels not blank
    Given Content validation
    When Checking legal link labels
    Then All legal link labels have non-empty descriptive text

  Scenario: Legal page moved handled
    Given Legal page URL changed
    When User clicks legal link
    Then Redirect in place or broken link detected in monitoring

  Scenario: Long labels handled gracefully
    Given Legal link label is very long
    When Footer renders
    Then Long label displays without breaking footer layout

  Scenario: Locale variant handled
    Given Site supports multiple locales
    When Checking legal links
    Then Legal links appropriate for current locale display or fallback
