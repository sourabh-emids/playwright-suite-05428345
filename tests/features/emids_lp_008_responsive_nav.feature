Feature: Provide responsive accessible navigation

    @emids_lp_008
    Scenario: verify_menu_open_close_without_hover
        Given User is on touch device or prefers reduced motion
        When User taps menu trigger
        Then Menu can be opened and closed without requiring hover

    @emids_lp_008
    Scenario: verify_escape_closes_overlays
        Given An open menu or overlay exists
        When User presses Escape key
        Then Open overlays close and focus returns appropriately

    @emids_lp_008
    Scenario: verify_visible_focus_maintained
        Given User navigates through page using keyboard
        When Focus moves between interactive elements
        Then Visible focus indicator is maintained on all focusable elements

    @emids_lp_008
    Scenario: verify_no_horizontal_scroll_at_supported_widths
        Given User views page at supported viewport widths
        When Page content renders
        Then Content reflows without horizontal page scrolling

    @emids_lp_008
    Scenario: verify_interactive_controls_semantic
        Given Interactive navigation controls exist
        When Automated check validates control semantics
        Then All controls use semantic button or link elements

    @emids_lp_008
    Scenario: verify_focus_order_matches_visual_order
        Given User tabs through page
        When Focus order is evaluated
        Then Focus order matches visual reading order

    @emids_lp_008
    Scenario: verify_resize_while_menu_open
        Given Navigation menu is open
        When User resizes browser window
        Then Menu state is preserved or gracefully transitioned without breaking

    @emids_lp_008
    Scenario: verify_orientation_change_handling
        Given User changes device orientation
        When Page reflows to new orientation
        Then Navigation remains accessible and functional

    @emids_lp_008
    Scenario: verify_browser_zoom_200_percent
        Given User sets browser zoom to 200%
        When Page renders
        Then Navigation and content remain usable without horizontal scrolling

    @emids_lp_008
    Scenario: verify_reduced_motion_respected
        Given User has prefers_reduced_motion enabled
        When Page renders navigation with animations
        Then Motion animations are reduced or disabled per user preference

    @emids_lp_008
    Scenario: verify_js_partial_failure_handling
        Given JavaScript partially fails during page load
        When Page continues rendering
        Then Core navigation remains functional and accessible
