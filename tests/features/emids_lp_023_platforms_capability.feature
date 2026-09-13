"""Feature: Render Platforms capability content (emids_lp_023)."""
Feature: Render Platforms capability content

    @emids_lp_023 @capabilities @platforms
    Scenario: Platforms capability content renders
        Given User views Platforms capability card/panel
        When Content loads
        Then Platforms label displays
        And Supporting content renders correctly

    @emids_lp_023 @capabilities @platforms
    Scenario: Labels consistent with navigation
        Given User compares Platforms capability to header navigation
        When User checks terminology
        Then Navigation and body copy use same approved taxonomy label
        And No 'Provider Platforms' vs 'Platforms' mismatch

    @emids_lp_023 @capabilities @platforms
    Scenario: Content governance prevents inconsistent synonyms
        Given CMS content is managed
        When Content publishes
        Then Navigation and body copy use consistent terminology
        And No unintended synonyms

    @emids_lp_023 @capabilities @platforms
    Scenario: Stale CMS content detection
        Given CMS content is outdated
        When Page renders
        Then Current content displays
        And No stale terminology visible
