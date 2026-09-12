Feature: Responsive and accessible navigation behavior

  Scenario: Menu operation without hover
    Given A user on touch device or with hover disabled
    When Menu trigger is tapped
    Then Menu opens without requiring hover interaction

  Scenario: Escape closes open overlays
    Given A mega-menu or navigation overlay is open
    When User presses Escape key
    Then Overlay closes and focus returns appropriately

  Scenario: Visible focus is maintained
    Given User navigates through navigation elements
    When Tab key is pressed
    Then Visible focus indicator is present on active element at all times

  Scenario: Content reflows without horizontal scrolling
    Given The navigation at supported viewport widths
    When Responsive layouts are tested at each breakpoint
    Then No horizontal page scrolling occurs; content reflows appropriately

  Scenario: Interactive controls are semantic buttons/links
    Given Navigation interactive elements
    When Elements are inspected
    Then All interactive controls use semantic button or link elements

  Scenario: Focus order matches visual order
    Given Navigation structure
    When Focus order is tested
    Then Focus order follows visual layout order

  Scenario: Reduced motion preference respected
    Given User has prefers-reduced-motion enabled
    When Navigation animations are triggered
    Then Animations are reduced or disabled

  Scenario: Resize while menu open
    Given A menu is open and user resizes window
    When Breakpoint is crossed
    Then Menu state adapts appropriately without breaking layout

  Scenario: Browser zoom 200% support
    Given Browser zoom is set to 200%
    When Navigation is tested
    Then All navigation remains functional and readable
