"""Feature file for Issue 0008 - Responsive and accessible navigation behavior."""
Feature: Responsive and accessible navigation behavior

  Scenario: Menu can be opened/closed without hover
    Given A user is on a touch device or prefers no hover
    When The user taps the menu trigger
    Then The menu opens/closes correctly without requiring hover

  Scenario: Escape closes open overlays
    Given A mega-menu or mobile navigation overlay is open
    When The user presses the Escape key
    Then All open overlays close

  Scenario: Visible focus maintained throughout navigation
    Given A user is navigating the site with keyboard
    When The user tabs through interactive elements
    Then Visible focus is maintained on all interactive elements

  Scenario: Content reflows without horizontal scrolling
    Given A user resizes the browser window to various widths
    When The viewport changes between desktop, tablet, and mobile widths
    Then Content reflows without causing horizontal page scrolling

  Scenario: Interactive controls are semantic buttons/links
    Given A user or assistive technology examines navigation controls
    When The user inspects the HTML markup
    Then All interactive controls use semantic button or link elements

  Scenario: Reduced motion preference respected
    Given A user has prefers-reduced-motion enabled in their OS/browser
    When The user views the navigation
    Then Navigation animations are reduced or eliminated per user preference

  Scenario: Resize while menu open
    Given A mega-menu is open and the user resizes the window
    When The viewport changes breakpoint (e.g., desktop to mobile)
    Then The menu state adapts appropriately to the new breakpoint

  Scenario: Browser zoom 200% functional
    Given A user has set browser zoom to 200%
    When The user views and interacts with the navigation
    Then All navigation remains functional and content does not overlap
