Feature: Cookie Preferences control in footer

  Scenario: Cookie Preferences visible in footer
    Given Footer section
    When Footer content is verified
    Then Cookie Preferences control is visible

  Scenario: Activating opens consent-management UI
    Given Cookie Preferences control
    When Clicked
    Then Consent-management UI opens

  Scenario: User can revise or withdraw consent
    Given Consent management is open
    When User adjusts preferences
    Then User can revise or withdraw consent

  Scenario: Control available after initial banner dismissal
    Given Initial cookie banner has been dismissed
    When User returns to page or later session
    Then Cookie Preferences control remains available in footer

  Scenario: Consent script blocked handling
    Given Edge case where consent script is blocked
    When Page renders
    Then Footer remains functional and control attempts to show appropriate state
