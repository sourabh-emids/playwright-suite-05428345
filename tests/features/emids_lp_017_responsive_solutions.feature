"""Feature: Support featured-solution responsive interaction (emids_lp_017)."""
Feature: Support featured-solution responsive interaction

    @emids_lp_017 @featured-solutions @accessibility
    Scenario: Every solution reachable on keyboard
        Given User navigates with keyboard only
        When User tabs through Featured Solutions
        Then Every solution card is reachable and activatable via keyboard

    @emids_lp_017 @featured-solutions @mobile
    Scenario: Every solution reachable on touch
        Given User views Featured Solutions on touch device
        When User swipes or scrolls through solutions
        Then Every solution card is accessible and tappable

    @emids_lp_017 @featured-solutions
    Scenario: No content permanently hidden off-screen
        Given User views Featured Solutions section
        When User scrolls and interacts with layout
        Then All six solutions are discoverable
        And No solution requires specific gesture to access

    @emids_lp_017 @featured-solutions @accessibility
    Scenario: Carousel controls have accessible labels
        Given Design uses carousel for solutions
        When User examines navigation controls
        Then Previous/next controls have accessible labels
        And Active index is communicated

    @emids_lp_017 @featured-solutions @reduced-motion
    Scenario: Autoplay respects reduced motion
        Given Carousel autoplay is implemented
        When User has prefers-reduced-motion enabled
        Then Autoplay is disabled or meaningfully reduced
        And User can control playback

    @emids_lp_017 @featured-solutions @responsive
    Scenario: Viewport resize mid-interaction
        Given User is interacting with solutions on tablet
        When User resizes to mobile width
        Then Interaction state adapts
        And No frozen carousel
        And Content accessible

    @emids_lp_017 @featured-solutions
    Scenario: First/last item handling
        Given Carousel navigation is at first item
        When User clicks previous
        Then Appropriate wrap-around or boundary behavior occurs

    @emids_lp_017 @featured-solutions @mobile @accessibility
    Scenario: Swipe and keyboard conflict resolution
        Given User on touch device with keyboard
        When User uses both swipe and keyboard
        Then Both interaction methods work without conflict or data loss
