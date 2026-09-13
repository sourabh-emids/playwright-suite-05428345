Feature: Render Platforms capability content

    @emids_lp_023
    Scenario: verify_platforms_content_renders
        Given Platforms capability section renders
        When User views Platforms capability content
        Then Platforms content displays correctly

    @emids_lp_023
    Scenario: verify_labels_consistent_across_nav_body
        Given Platforms capability renders
        When Automated check compares navigation and body labels
        Then Labels use approved taxonomy consistently (e.g., 'Platforms' not 'Provider Platforms' in navigation)

    @emids_lp_023
    Scenario: verify_content_governance_prevents_inconsistency
        Given CMS content for Platforms capability
        When Content is validated before publish
        Then Inconsistent synonyms are prevented unless intentionally approved

    @emids_lp_023
    Scenario: verify_navigation_body_naming_match
        Given Platforms navigation item and body content
        When Automated check compares terminology
        Then Navigation and body copy use matching approved taxonomy

    @emids_lp_023
    Scenario: verify_stale_cms_content_detection
        Given CMS contains outdated Platforms taxonomy
        When Content validation runs
        Then Validation catches stale taxonomy before production

    @emids_lp_023
    Scenario: verify_platforms_card_visual_system
        Given Platforms capability card renders
        When User views card design
        Then Card matches capability visual system styling
