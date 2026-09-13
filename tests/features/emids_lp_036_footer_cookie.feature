"""Feature: Expose Cookie Preferences control (emids_lp_036)."""
Feature: Expose Cookie Preferences control

    @emids_lp_036 @footer
    Scenario: Cookie Preferences visible in footer
        Given User views page footer
        When User locates cookie control
        Then Cookie Preferences control is visible

    @emids_lp_036 @footer
    Scenario: Activating opens consent management UI
        Given User clicks Cookie Preferences
        When Control activates
        Then Consent management UI opens
        And User can revise or withdraw consent

    @emids_lp_036 @footer
    Scenario: Control available after initial banner dismissal
        Given Initial cookie banner is dismissed
        When User searches for cookie control
        Then Cookie Preferences remains accessible in footer
