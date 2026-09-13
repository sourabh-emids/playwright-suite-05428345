Feature: Support featured-solution responsive interaction

  Scenario: Verify every solution reachable on keyboard
    Given Featured Solutions section renders (cards, rail, or carousel)
    When User navigates via keyboard
    Then Every solution is reachable and selectable via keyboard

  Scenario: Verify every solution reachable on touch
    Given Featured Solutions section renders on touch device
    When User interacts via touch
    Then Every solution is reachable via swipe or touch

  Scenario: Verify no content permanently hidden off-screen
    Given Featured Solutions use carousel or rail layout
    When User navigates through content
    Then All solutions are accessible; content is not permanently hidden

  Scenario: Verify carousel controls have accessible labels
    Given Carousel controls exist
    When Screen reader reads controls
    Then Previous/next controls have accessible labels describing their function

  Scenario: Verify autoplay respects reduced motion
    Given User prefers reduced motion
    When Autoplay carousel exists
    Then Autoplay is disabled or uses minimal animation

  Scenario: Verify viewport resize mid-interaction
    Given User is interacting with carousel
    When Viewport resizes
    Then Interaction state is maintained or gracefully reset

  Scenario: Verify first/last item navigation
    Given User navigates carousel to first item
    When User presses previous control
    Then Behavior is intuitive (wrap or stop) per design specification

  Scenario: Verify swipe and keyboard do not conflict
    Given User is on touch device with keyboard
    When User swipes then uses keyboard
    Then Focus and scroll position do not conflict unexpectedly
