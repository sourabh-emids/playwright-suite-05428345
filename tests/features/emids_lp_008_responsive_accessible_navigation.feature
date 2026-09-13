"""Feature: Responsive accessible navigation behavior (emids_lp_008)."""
Feature: Responsive accessible navigation behavior

    @emids_lp_008 @navigation @accessibility
    Scenario: Menu open close without hover
        Given User is on desktop with keyboard or touch
        When User activates any menu trigger
        Then Menu opens without requiring hover
        And Toggle works predictably

    @emids_lp_008 @navigation
    Scenario: Escape closes open overlays
        Given Any navigation menu is open
        When User presses Escape key
        Then Menu closes
        And Focus is managed appropriately

    @emids_lp_008 @navigation @accessibility
    Scenario: Visible focus maintained
        Given User navigates through header with keyboard
        When User tabs between interactive elements
        Then Focus indicator is visible on all interactive elements

    @emids_lp_008 @navigation @responsive
    Scenario: Content reflows without horizontal scrolling
        Given User views site at supported widths including 320px
        When Page renders
        Then Content reflows appropriately
        And No horizontal scrollbar appears

    @emids_lp_008 @navigation
    Scenario: Interactive controls are semantic buttons or links
        Given User examines navigation controls
        When User inspects control elements
        Then Controls use semantic HTML buttons or links
        And No div-based click handlers

    @emids_lp_008 @navigation @accessibility
    Scenario: Focus order matches visual order
        Given User navigates header with keyboard
        When User tabs through navigation
        Then Focus order follows visual layout order

    @emids_lp_008 @navigation @responsive
    Scenario: Resize while menu open handling
        Given Navigation menu is open on desktop
        When User resizes browser to mobile width
        Then Menu state adjusts appropriately for new breakpoint
        And No frozen or broken state

    @emids_lp_008 @navigation @accessibility @reduced-motion
    Scenario: Reduced motion preference respected
        Given User has prefers-reduced-motion enabled
        When User interacts with navigation
        Then No non-essential continuous animations play

    @emids_lp_008 @navigation @accessibility
    Scenario: Browser zoom 200% support
        Given User sets browser zoom to 200%
        When User views and navigates header
        Then Navigation remains functional
        And Content readable without horizontal scrolling

    @emids_lp_008 @navigation
    Scenario: JS partial failure handling
        Given JavaScript partially fails during page load
        When Page renders
        Then Core navigation remains functional
        And Basic links and menu structure work
