Feature: Expose Cookie Preferences control

  Scenario: Cookie Preferences visible in footer
    Given User views page footer
    When Locating cookie control
    Then Cookie Preferences link or button is visible in footer

  Scenario: Cookie control opens consent management UI
    Given User clicks Cookie Preferences
    When Activation occurs
    Then Consent management interface opens

  Scenario: User can revise or withdraw consent
    Given Consent UI is open
    When User adjusts consent choices
    Then User can modify consent preferences and save changes

  Scenario: Control available after initial banner dismissal
    Given User dismissed initial cookie banner
    When Returning to page later or scrolling
    Then Cookie Preferences control remains accessible in footer

  Scenario: Consent script blocked handled
    Given Consent management script blocked
    When User clicks Cookie Preferences
    Then Fallback experience or error message displays

  Scenario: Storage disabled handled
    Given Browser storage is disabled
    When User attempts to save consent
    Then Consent state handled gracefully; user informed of limitation

  Scenario: User clears cookies handled
    Given User clears browser cookies
    When Returning to site
    Then Cookie Preferences allows user to re-establish consent
