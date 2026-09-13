Feature: Maintain semantic section hierarchy

    @emids_lp_014
    Scenario: verify_single_page_h1
        Given Page renders fully
        When Automated check scans for H1 elements
        Then Exactly one page-level H1 exists on the entire landing page

    @emids_lp_014
    Scenario: verify_subsequent_headings_logical_levels
        Given Page contains multiple section headings
        When Automated check validates heading hierarchy
        Then Subsequent section headings use logical levels (H2, H3, etc.) without skipped levels where avoidable

    @emids_lp_014
    Scenario: verify_landmarks_identifiable
        Given Page renders
        When Automated accessibility check runs
        Then main, header, footer landmarks are identifiable and properly structured

    @emids_lp_014
    Scenario: verify_interactive_text_not_headings_for_styling
        Given Interactive text elements exist
        When Automated check validates semantics
        Then Interactive text is not using headings solely for styling purposes

    @emids_lp_014
    Scenario: verify_cms_duplicate_h1_detection
        Given CMS content results in duplicate H1
        When Page renders
        Then Validation catches duplicate H1 before production or renders with single H1

    @emids_lp_014
    Scenario: verify_hidden_heading_not_focusable
        Given Hidden heading exists in page structure
        When User navigates via keyboard
        Then Hidden headings do not become unexpectedly focusable
