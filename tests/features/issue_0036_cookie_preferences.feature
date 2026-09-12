"""Feature file for Issue 0036 - Cookie Preferences control exposure."""
Feature: Cookie Preferences control exposure

  Scenario: Cookie Preferences control visible in footer
    Given A user views the footer
    When The footer loads
    Then Cookie Preferences control (link/button) is visible

  Scenario: Control activates consent-management UI
    Given A user clicks the Cookie Preferences control
    When The control is activated
    Then The consent-management UI opens

  Scenario: User can revise or withdraw consent
    Given A user has previously given consent
    When The user opens Cookie Preferences
    Then User can revise or withdraw consent

  Scenario: Control available after initial banner dismissal
    Given A user has dismissed the initial cookie banner
    When The user returns to the footer
    Then Cookie Preferences control remains available

  Scenario: Consent script blocked handling
    Given Consent script is blocked (by browser or CSP)
    When The page loads
    Then Page remains functional; consent controls are not blocking dependencies

  Scenario: Storage disabled handling
    Given Browser storage is disabled
    When User attempts to save consent preferences
    Then Appropriate handling occurs (user informed, alternative storage attempted, or graceful degradation)
