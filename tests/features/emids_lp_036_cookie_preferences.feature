Feature: Expose Cookie Preferences control on every page

  Scenario: Verify Cookie Preferences visible in footer
    Given User views footer on any page
    When User locates Cookie Preferences control
    Then Control is visible and accessible in the footer

  Scenario: Verify activating opens consent-management UI
    Given Cookie Preferences control is visible
    When User clicks or activates the control
    Then Consent-management UI opens

  Scenario: Verify user can revise or withdraw consent
    Given Consent-management UI is open
    When User modifies consent choices
    Then User can revise or withdraw consent preferences

  Scenario: Verify control available after banner dismissal
    Given Cookie banner has been dismissed
    When User returns to page or navigates to different page
    Then Cookie Preferences control remains available in footer

  Scenario: Verify consent script blocked handled
    Given Consent script is blocked by browser or extension
    When Page loads
    Then Page remains functional; Cookie Preferences control shows appropriate fallback

  Scenario: Verify storage disabled handled
    Given Browser local storage is disabled
    When User interacts with consent preferences
    Then Consent state persists in memory or user is notified of limitations

  Scenario: Verify user clears cookies handled
    Given User has cleared browser cookies
    When User returns to page
    Then Cookie Preferences control remains available; consent state resets appropriately
