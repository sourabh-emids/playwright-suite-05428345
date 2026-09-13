Feature: WCAG 2.1 AA compliance

    @emids_lp_050
    Scenario: verify_keyboard_access
        Given All interactive elements on page
        When User navigates via keyboard only
        Then All functionality is accessible without mouse

    @emids_lp_050
    Scenario: verify_visible_focus
        Given User navigates via keyboard
        When Focus moves between elements
        Then Visible focus indicator is maintained

    @emids_lp_050
    Scenario: verify_semantic_landmarks
        Given Page renders
        When Accessibility tool scans structure
        Then Semantic landmarks (header, main, footer, nav) are identifiable

    @emids_lp_050
    Scenario: verify_sufficient_contrast
        Given Text and interactive elements render
        When Automated contrast check runs
        Then Contrast ratios meet WCAG AA minimums (4.5:1 normal text, 3:1 large text)

    @emids_lp_050
    Scenario: verify_meaningful_alt_text
        Given Images and media render
        When Screen reader or automated check validates
        Then Meaningful alt text is provided; decorative elements marked appropriately

    @emids_lp_050
    Scenario: verify_accessible_names
        Given Interactive elements render
        When Accessibility check runs
        Then All interactive elements have accessible names

    @emids_lp_050
    Scenario: verify_200_zoom_reflow_support
        Given Page at 200% zoom
        When Content reflows
        Then Content is reflowed without horizontal scrolling

    @emids_lp_050
    Scenario: verify_form_errors_accessible
        Given Form has validation errors
        When User submits invalid form
        Then Errors are accessible and associated with fields

    @emids_lp_050
    Scenario: verify_reduced_motion_handling
        Given User prefers reduced motion
        When Page with animations renders
        Then Motion is reduced per user preference

    @emids_lp_050
    Scenario: verify_media_alternatives
        Given Video/audio media exists
        When Accessibility check runs
        Then Captions, transcripts, or alternatives are provided

    @emids_lp_050
    Scenario: verify_no_color_only_information
        Given Color conveys information
        When Automated check validates
        Then Information is not conveyed by color alone

    @emids_lp_050
    Scenario: verify_touch_target_size
        Given Interactive touch targets exist
        When Accessibility check validates
        Then Touch targets meet minimum size requirements (44x44px)

    @emids_lp_050
    Scenario: verify_high_contrast_mode
        Given Windows High Contrast mode enabled
        When Page renders
        Then Page remains functional and visible

    @emids_lp_050
    Scenario: verify_forced_colors_mode
        Given Forced colors mode enabled
        When Page renders
        Then Page handles forced colors appropriately
