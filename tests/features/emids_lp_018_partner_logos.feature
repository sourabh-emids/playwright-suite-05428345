Feature: Render partner logo rail/marquee

    @emids_lp_018
    Scenario: verify_all_approved_logos_render
        Given Partnerships section renders
        When User views partner logos
        Then All approved partner logos are displayed: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

    @emids_lp_018
    Scenario: verify_logos_meaningful_accessible_names
        Given Partner logos render
        When Screen reader reads logos
        Then Each logo has meaningful accessible name (partner name) unless treated as decorative with adjacent text

    @emids_lp_018
    Scenario: verify_no_duplicate_announcements
        Given DOM uses looping for marquee animation
        When Screen reader or DOM reader analyzes content
        Then Logical partner list does not duplicate for assistive technologies

    @emids_lp_018
    Scenario: verify_logo_asset_required
        Given Partner data is configured
        When Page renders
        Then Logo asset is present for each partner; missing logo shows placeholder

    @emids_lp_018
    Scenario: verify_horizontal_logo_sequence
        Given Partners section renders
        When User views layout
        Then Logos display in horizontal sequence

    @emids_lp_018
    Scenario: verify_marquee_loops_if_used
        Given Design requires looping marquee
        When Animation runs
        Then Marquee loops smoothly without jarring restart

    @emids_lp_018
    Scenario: verify_missing_logo_handling
        Given Partner logo asset is missing
        When Section renders
        Then Placeholder or fallback is shown; page does not break

    @emids_lp_018
    Scenario: verify_transparent_logo_visibility
        Given Partner logo has transparent background
        When Logo renders on various backgrounds
        Then Logo remains visible and readable
