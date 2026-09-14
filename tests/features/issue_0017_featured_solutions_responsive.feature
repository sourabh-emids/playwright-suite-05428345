Feature: Support featured-solution responsive interaction

  Scenario: Every solution reachable on keyboard
    Given User navigates Featured Solutions via keyboard
    When Pressing Tab or Arrow keys
    Then Each of the six solutions receives focus

  Scenario: Every solution reachable on touch
    Given User is on touch device
    When Swiping or tapping through solutions
    Then All solutions are discoverable and accessible

  Scenario: No content hidden permanently off-screen
    Given User views Featured Solutions on smallest supported viewport
    When Checking content visibility
    Then All solution content is accessible via scrolling or swipe; none permanently hidden

  Scenario: Carousel controls have accessible labels
    Given Featured Solutions uses carousel pattern
    When Checking carousel controls
    Then Previous/Next controls have accessible labels (e.g., 'Previous solution', 'Next solution')

  Scenario: Autoplay respects reduced motion
    Given User has prefers-reduced-motion enabled
    When Page with autoplay carousel renders
    Then Autoplay is disabled or reduced; user can still control manually

  Scenario: Autoplay does not prevent user control
    Given Carousel is autoplaying
    When User interacts with carousel
    Then User interaction immediately takes control; autoplay pauses

  Scenario: Viewport resize mid-interaction handled
    Given User is interacting with carousel on tablet
    When Window resizes to mobile width
    Then Layout transitions smoothly; interaction state is preserved

  Scenario: First and last item navigation works
    Given User is on first solution item
    When Clicking Previous or navigating backward
    Then Behavior is intuitive (wraps to last or stops appropriately)

  Scenario: Swipe and keyboard conflict resolution
    Given User uses both swipe and keyboard on touch device
    When Interactions overlap
    Then Interactions work harmoniously without conflict or unexpected behavior
