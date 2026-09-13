Feature: Provide responsive and accessible navigation behavior

  Scenario: Verify menu can be opened without hover
    Given The user is on a touch device or has hover disabled
    When The user activates a navigation control
    Then The menu opens without requiring hover interaction

  Scenario: Verify Escape closes open overlays
    Given A navigation menu or overlay is open
    When The user presses the Escape key
    Then The open overlay or menu closes

  Scenario: Verify visible focus is maintained
    Given The user navigates through interactive elements using keyboard
    When Focus moves between elements
    Then A visible focus indicator is maintained on all interactive elements

  Scenario: Verify content reflows without horizontal scrolling
    Given The user is viewing at supported viewport widths (320px to 1920px)
    When The page renders or is resized
    Then Content reflows appropriately without requiring horizontal page scrolling

  Scenario: Verify resize while menu open
    Given A navigation menu is currently open
    When The user resizes the viewport
    Then The menu state is handled gracefully, either closing or adapting to the new viewport

  Scenario: Verify orientation change handled
    Given The user is on a mobile device
    When The device orientation changes from portrait to landscape or vice versa
    Then Navigation remains functional and properly laid out

  Scenario: Verify browser zoom at 200% supported
    Given The user has browser zoom set to 200%
    When The user views the navigation
    Then Navigation remains usable and content does not overlap or become inaccessible

  Scenario: Verify JS partial failure handled
    Given JavaScript partially fails during page load
    When The user attempts to use navigation
    Then Core navigation remains functional using semantic HTML fallback

  Scenario: Verify reduced motion preference respected
    Given User has prefers-reduced-motion set
    When Navigation animations are triggered
    Then Animations are disabled or meaningfully reduced
