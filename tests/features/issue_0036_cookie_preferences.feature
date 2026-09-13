Feature: Cookie Preferences control exposure

  Scenario: Cookie Preferences visible in footer
    Given User views Emids homepage footer
    When Page renders
    Then Cookie Preferences control is visible in the footer

  Scenario: Activating opens consent UI
    Given User is on Emids homepage
    When User clicks Cookie Preferences control
    Then Consent-management UI opens

  Scenario: User can revise consent
    Given Consent UI is open
    When User modifies consent choices
    Then User can revise or withdraw consent

  Scenario: Control available after initial banner dismissal
    Given Cookie consent banner has been dismissed
    When User returns to any page
    Then Cookie Preferences control remains available in footer

  Scenario: Consent script blocked handling
    Given Consent script is blocked
    When User clicks Cookie Preferences
    Then Appropriate fallback or message displays

  Scenario: Storage disabled handling
    Given Browser storage is disabled
    When User attempts to save consent
    Then Graceful degradation occurs

  Scenario: User clears cookies handling
    Given User clears cookies
    When User returns to site
    Then Cookie Preferences control remains functional
