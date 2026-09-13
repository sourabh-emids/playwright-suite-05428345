Feature: Render 1 Day 2 Weeks 3 Months message

    @emids_lp_035
    Scenario: verify_timing_labels_render_ordered
        Given Final CTA section renders
        When User views timing message
        Then All timing labels render in order: 1 Day, 2 Weeks, 3 Months

    @emids_lp_035
    Scenario: verify_screen_reader_timing_content
        Given Timing message renders with visual styling
        When Screen reader interprets content
        Then Timing labels are understandable to screen readers (not encoded visually alone)

    @emids_lp_035
    Scenario: verify_meaning_not_visual_styling_alone
        Given Timing message data
        When Automated check validates encoding
        Then Meaning is not conveyed through visual styling alone; text content is present

    @emids_lp_035
    Scenario: verify_explanatory_labels_configured
        Given Timing message includes explanations
        When User views content
        Then Explanatory labels display if configured alongside timing values

    @emids_lp_035
    Scenario: verify_mobile_wrapping
        Given Timing message renders at mobile width
        When Page reflows
        Then Labels wrap appropriately without breaking layout

    @emids_lp_035
    Scenario: verify_missing_explanation_handling
        Given Explanatory label is missing
        When Section renders
        Then Timing values still render meaningfully without explanation
