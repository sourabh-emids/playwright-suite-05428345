Feature: Responsive accessible navigation
  # issue_0008

  Scenario: Menu opens and closes without hover requirement
    Given A user is on a touch device without hover capability
    When The user taps a navigation item
    Then The menu opens without requiring hover

  Scenario: Escape key closes open overlays
    Given A menu is currently open
    When The user presses the Escape key
    Then The open menu or overlay closes

  Scenario: Visible focus is maintained throughout navigation
    Given A user navigates through the page using keyboard
    When Focus moves between interactive elements
    Then A visible focus indicator is maintained on all interactive elements

  Scenario: Content reflows without horizontal scrolling
    Given A user views the page at various supported viewport widths
    When The browser window is resized
    Then Content reflows cleanly and no horizontal scrollbar appears

  Scenario: Reduced motion preference is respected
    Given A user has prefers-reduced-motion enabled in their system
    When The page renders or contains animations
    Then Continuous animations are disabled or reduced

  Scenario: Resize while menu open handled properly
    Given A navigation menu is currently open
    When The user resizes the browser window
    Then The menu state updates appropriately without breaking layout

  Scenario: Breakpoint transitions work correctly
    Given A user is viewing at a specific breakpoint
    When The viewport crosses a breakpoint threshold
    Then The navigation layout transitions correctly between desktop mega-menu and mobile disclosure
