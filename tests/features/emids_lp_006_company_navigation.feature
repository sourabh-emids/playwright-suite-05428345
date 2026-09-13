"""Feature: Implement Company navigation group (emids_lp_006)."""
Feature: Implement Company navigation group

    @emids_lp_006 @company-nav
    Scenario: Company menu exposes approved links
        Given User opens Company menu
        When User views available company links
        Then All displayed links are published/approved pages
        And Contact/Connect destinations are included

    @emids_lp_006 @company-nav
    Scenario: Company navigation works with keyboard, pointer, and touch
        Given User navigates to Company menu
        When User activates menu via keyboard, mouse click, or touch
        Then Menu opens in all interaction modes
        And Links are accessible

    @emids_lp_006 @company-nav
    Scenario: Redirect loop prevention
        Given User navigates to Company pages
        When User clicks company navigation links
        Then No redirect loops occur
        And Pages load within reasonable time

    @emids_lp_006 @company-nav
    Scenario: Unpublished page handling
        Given A company page is unpublished
        When User opens Company menu
        Then Unpublished page does not appear in navigation
