"""Feature: Responsive Accessible Navigation Behavior."""
Feature: Responsive Accessible Navigation Behavior

  @issue_0008
  Scenario: menu_open_close_without_hover
    Given User is on touch or non-hover device
    When User activates menu trigger
    Then Menu can be opened/closed without hover requirement

  @issue_0008
  Scenario: escape_closes_open_overlays
    Given Any overlay/menu is open
    When User presses Escape key
    Then Open overlays close

  @issue_0008
  Scenario: visible_focus_maintained
    Given User navigates via keyboard through page
    When Focus indicator is checked at each interactive element
    Then Visible focus is maintained throughout navigation

  @issue_0008
  Scenario: content_reflows_without_horizontal_scroll
    Given Page is rendered at supported widths (320px to desktop)
    When Viewport is resized
    Then Content reflows without horizontal page scrolling

  @issue_0008
  Scenario: interactive_controls_semantic
    Given Navigation interactive controls are inspected
    When HTML elements are reviewed
    Then Interactive controls are semantic buttons or links

  @issue_0008
  Scenario: focus_order_matches_visual_order
    Given User tabs through page
    When Focus order is compared to visual layout
    Then Focus order matches visual order

  @issue_0008
  Scenario: reduced_motion_preference_respected
    Given User has prefers-reduced-motion enabled
    When Page renders with animations
    Then Reduced motion preferences are respected

  @issue_0008
  Scenario: resize_while_menu_open
    Given Menu is open and viewport is resized
    When Viewport crosses breakpoint
    Then Menu state is handled appropriately without errors

  @issue_0008
  Scenario: browser_zoom_200_percent
    Given Browser zoom is set to 200%
    When User interacts with navigation
    Then All navigation remains functional and visible

  @issue_0008
  Scenario: js_partial_failure_handling
    Given JavaScript partially fails or loads incompletely
    When User interacts with navigation
    Then Core navigation remains functional via fallback
