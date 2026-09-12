Feature: Featured solution responsive interaction

  Scenario: Every solution reachable on keyboard
    Given Featured solutions section
    When Keyboard navigation is tested
    Then Every solution can be reached using Tab key

  Scenario: Every solution reachable on touch
    Given Featured solutions on touch device
    When Touch interaction is tested
    Then Every solution can be accessed via touch

  Scenario: No content permanently hidden
    Given Responsive layout options (cards, rail, carousel, stacked)
    When Layout is verified at all breakpoints
    Then No content is permanently hidden off-screen

  Scenario: Carousel controls have accessible labels
    Given If carousel is used for featured solutions
    When Controls are inspected
    Then Previous/next controls have accessible labels

  Scenario: Autoplay respects reduced motion
    Given Carousel with autoplay enabled
    When User has prefers-reduced-motion
    Then Autoplay does not prevent user control and respects reduced motion preference

  Scenario: Viewport resize during interaction
    Given User is interacting with carousel
    When Viewport is resized
    Then Interaction continues without breaking state
