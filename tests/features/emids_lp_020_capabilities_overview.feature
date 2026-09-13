Feature: Render capabilities overview

    @emids_lp_020
    Scenario: verify_three_capability_groups_visible
        Given Capabilities section renders
        When User views section content
        Then All three groups (AI, Engineering, Platforms) are visible with corresponding content/actions

    @emids_lp_020
    Scenario: verify_group_labels_match_navigation
        Given Capabilities section renders
        When Automated check validates labels
        Then Group labels match navigation taxonomy (AI, Engineering, Platforms)

    @emids_lp_020
    Scenario: verify_three_primary_groups_required
        Given Capabilities section renders
        When Automated check counts groups
        Then Exactly three primary groups are present for this content version

    @emids_lp_020
    Scenario: verify_responsive_capability_cards
        Given Capabilities section renders on mobile viewport
        When Content reflows
        Then Capability cards/panels adapt responsively

    @emids_lp_020
    Scenario: verify_missing_group_handling
        Given One capability group is missing from data
        When Section renders
        Then Validation catches missing group or graceful placeholder shown

    @emids_lp_020
    Scenario: verify_mislabeled_taxonomy_handling
        Given Capability group has incorrect label
        When Section renders
        Then Content governance validation catches mismatched taxonomy

    @emids_lp_020
    Scenario: verify_overflow_handling
        Given Capability cards have maximum content
        When Page renders at mobile width
        Then Overflow is handled gracefully without breaking layout
