Feature: Provide responsive accessible navigation

  Scenario: Menu can be opened closed without hover
    Given User is on touch device or keyboard-only navigation
    When User activates menu trigger via click or Enter
    Then Menu opens without requiring hover interaction

  Scenario: Escape key closes open overlays
    Given Any mega-menu or overlay is open
    When User presses Escape key
    Then All open overlays close

  Scenario: Visible focus is maintained throughout navigation
    Given User navigates through header using keyboard
    When Focus moves between interactive elements
    Then Focus indicator remains visible on all interactive elements

  Scenario: Content reflows without horizontal scrolling at supported widths
    Given User resizes browser to mobile, tablet, and desktop widths
    When Page renders at each breakpoint
    Then No horizontal scrolling occurs; content reflows appropriately

  Scenario: Interactive controls are semantic buttons or links
    Given User inspects header interactivity code
    When Checking HTML semantics
    Then Menu triggers use <button> or semantic link elements, not <div> with click handlers

  Scenario: Focus order matches visual order
    Given User navigates header using keyboard
    When Checking tab order
    Then Focus follows logical left-to-right, top-to-bottom sequence matching visual layout

  Scenario: Reduced motion preferences respected
    Given User has prefers-reduced-motion enabled
    When Page renders or animations would trigger
    Then Continuous animations are reduced or disabled

  Scenario: Resize while menu open handled gracefully
    Given Mega-menu is open during window resize
    When Viewport changes from desktop to mobile width
    Then Menu state transitions appropriately without error or visual glitch

  Scenario: Browser zoom 200% navigation usable
    Given User sets browser zoom to 200%
    When User attempts to use navigation
    Then Navigation remains fully functional without overlapping or clipping
