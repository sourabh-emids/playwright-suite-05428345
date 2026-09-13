"""Feature: Implement Capabilities mega-menu (emids_lp_003)."""
Feature: Implement Capabilities mega-menu

    @emids_lp_003 @capabilities-menu
    Scenario: Capabilities menu opens predictably
        Given User focuses on Capabilities navigation
        When User activates the Capabilities menu trigger
        Then Menu opens consistently
        And AI, Engineering, and Platforms groups are visible

    @emids_lp_003 @capabilities-menu
    Scenario: Capability links keyboard operable
        Given Capabilities mega-menu is open
        When User tabs through capability links
        Then All capability links receive focus
        And Links are keyboard navigable to destinations

    @emids_lp_003 @capabilities-menu
    Scenario: Labels match approved taxonomy
        Given Capabilities menu is open
        When User examines group labels
        Then Labels match approved site taxonomy
        And No duplicate labels within menu

    @emids_lp_003 @capabilities-menu @responsive
    Scenario: Mega-menu on desktop, disclosure on mobile
        Given User switches between desktop and mobile viewports
        When User activates Capabilities navigation
        Then Desktop shows mega-menu layout
        And Mobile shows accessible disclosure pattern

    @emids_lp_003 @capabilities-menu
    Scenario: Duplicate labels detection
        Given User opens Capabilities menu
        When User scans for duplicate labels
        Then No duplicate labels exist within the menu

    @emids_lp_003 @capabilities-menu @responsive
    Scenario: Menu overflow handling
        Given Capabilities menu is open with many items
        When User views menu on various viewport sizes
        Then Menu content remains visible and accessible
        And No overflow issues occur
