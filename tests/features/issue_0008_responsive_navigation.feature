Feature: Responsive and accessible navigation behavior

  Scenario: Menu can be opened/closed without hover
    Given User is on Emids homepage with touch device or keyboard-only access
    When User activates navigation trigger via tap or Enter
    Then Menu opens without requiring hover

  Scenario: Escape closes open overlays
    Given A navigation menu or overlay is open
    When User presses Escape key
    Then Open overlay closes

  Scenario: Visible focus is maintained
    Given User is navigating through header using keyboard
    When Focus moves between interactive elements
    Then Visible focus indicator is maintained on all interactive elements

  Scenario: Content reflows without horizontal scrolling
    Given User views Emids homepage at supported viewport widths
    When Page renders
    Then Content reflows cleanly without requiring horizontal page scrolling

  Scenario: Interactive controls are semantic
    Given User views header source code
    When User inspects interactive controls
    Then Interactive controls are semantic buttons or links

  Scenario: Focus order matches visual order
    Given User navigates header with keyboard
    When Focus order is observed
    Then Focus order matches visual order

  Scenario: Reduced motion preference respected
    Given User has prefers-reduced-motion enabled
    When User views navigation menus with animations
    Then Animations are reduced or disabled as appropriate

  Scenario: Resize while menu open
    Given Navigation menu is open at desktop width
    When User resizes to mobile width
    Then Menu state is handled gracefully with content accessible

  Scenario: Orientation change handled
    Given User is viewing Emids homepage in landscape
    When User changes to portrait orientation
    Then Navigation remains functional and accessible

  Scenario: Browser zoom at 200% supported
    Given User sets browser zoom to 200%
    When User views Emids homepage
    Then Content remains readable and navigation accessible

  Scenario: JS partial failure handling
    Given JavaScript partially fails during page load
    When User attempts to use navigation
    Then Core navigation links remain functional
