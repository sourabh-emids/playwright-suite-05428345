Feature: Featured solutions responsive interaction
  # issue_0017

  Scenario: Every solution reachable on keyboard
    Given The Featured Solutions section is rendered
    When Keyboard navigation testing runs
    Then Every solution card or item is reachable using Tab key

  Scenario: Every solution reachable on touch
    Given The page is viewed on a touch device
    When Touch testing validates interaction
    Then Every solution is accessible via touch

  Scenario: No content permanently hidden off-screen
    Given The Featured Solutions section is rendered at any viewport
    When Visual inspection runs
    Then All content is visible or accessible without requiring horizontal scrolling

  Scenario: Carousel controls have accessible labels if used
    Given The Featured Solutions section uses a carousel layout
    When Accessibility testing analyzes controls
    Then Previous/next controls have accessible labels or names

  Scenario: Autoplay respects reduced motion
    Given The Featured Solutions uses an autoplay carousel
    When User has prefers-reduced-motion enabled
    Then Autoplay is disabled or meaningfully reduced

  Scenario: Viewport resize during interaction handled
    Given User is interacting with Featured Solutions
    When Viewport is resized mid-interaction
    Then The interaction state updates appropriately without breaking
