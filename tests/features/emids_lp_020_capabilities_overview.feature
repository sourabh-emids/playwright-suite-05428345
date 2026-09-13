"""Feature: Render capabilities overview (emids_lp_020)."""
Feature: Render capabilities overview

    @emids_lp_020 @capabilities
    Scenario: All three capability groups visible
        Given User views Capabilities section
        When User scans for groups
        Then AI, Engineering, and Platforms groups are all visible

    @emids_lp_020 @capabilities
    Scenario: Each group has corresponding content
        Given User examines each capability group
        When User reads group content
        Then Each group contains title, summary, and relevant links/media

    @emids_lp_020 @capabilities
    Scenario: Group labels match navigation taxonomy
        Given User compares capabilities section to header navigation
        When User checks terminology
        Then Labels are consistent: AI, Engineering, Platforms match navigation taxonomy

    @emids_lp_020 @capabilities
    Scenario: Three primary groups required
        Given CMS content is managed
        When Page renders
        Then Exactly three primary groups display
        And No missing or extra groups

    @emids_lp_020 @capabilities @responsive
    Scenario: Responsive capability cards layout
        Given User views Capabilities on mobile
        When Page renders
        Then Cards/panels reflow appropriately
        And No overflow or hidden content

    @emids_lp_020 @capabilities
    Scenario: Group missing handling
        Given One capability group is not configured
        When Page renders
        Then Section handles missing group gracefully
        And Remaining groups display correctly
