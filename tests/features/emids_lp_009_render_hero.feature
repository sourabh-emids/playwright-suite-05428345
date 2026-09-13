"""Feature: Render hero messaging and visual (emids_lp_009)."""
Feature: Render hero messaging and visual

    @emids_lp_009 @hero
    Scenario: Primary H1 present on hero
        Given User navigates to homepage
        When Page renders
        Then Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'

    @emids_lp_009 @hero
    Scenario: Supporting content readable
        Given Hero section renders
        When User reads hero content
        Then Body copy is visible and readable
        And Media has appropriate alternative handling

    @emids_lp_009 @hero
    Scenario: Hero CTA visible above deep page scrolling
        Given User views homepage on common desktop sizes
        When Page loads
        Then CTA is visible without scrolling past the hero section

    @emids_lp_009 @hero
    Scenario: H1 non-empty and unique
        Given User examines page structure
        When User searches for H1 elements
        Then Exactly one H1 exists
        And H1 content is non-empty

    @emids_lp_009 @hero
    Scenario: Media URL resolves
        Given Hero includes media elements
        When User checks media source URLs
        Then Media URLs resolve successfully
        And Decorative media does not create redundant screen-reader output

    @emids_lp_009 @hero
    Scenario: Slow media handling
        Given Media assets load slowly
        When Page renders
        Then Text content renders while media loads
        And No blocking of critical content

    @emids_lp_009 @hero @responsive
    Scenario: Small viewport hero display
        Given User views site on mobile viewport
        When Page renders hero section
        Then Hero scales appropriately
        And Text remains readable
        And CTA accessible

    @emids_lp_009 @hero @reduced-motion
    Scenario: Reduced motion on hero
        Given User has prefers-reduced-motion enabled
        When Hero includes animations or video
        Then Motion reduced or disabled
        And Content remains accessible
