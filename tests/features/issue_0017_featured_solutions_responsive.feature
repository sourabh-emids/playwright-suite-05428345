Feature: Featured solution responsive interaction

  Scenario: Every solution reachable on keyboard
    Given Featured Solutions section uses interactive layout
    When User navigates with Tab key
    Then Every solution can be reached via keyboard

  Scenario: Every solution reachable on touch
    Given Featured Solutions section uses interactive layout
    When User navigates via touch
    Then Every solution can be reached via touch

  Scenario: No content permanently hidden off-screen
    Given Featured Solutions section renders
    When User tests at various viewport widths
    Then No content is permanently hidden off-screen

  Scenario: Carousel controls have accessible labels
    Given Featured Solutions uses carousel layout
    When User views carousel controls
    Then Previous/next controls have accessible labels

  Scenario: Autoplay respects reduced motion
    Given Carousel has autoplay enabled and user prefers reduced motion
    When Page renders
    Then Autoplay does not prevent user control and respects reduced motion preference

  Scenario: Viewport resize mid-interaction
    Given User is interacting with featured solutions at desktop
    When User resizes to mobile
    Then Interaction state is handled gracefully

  Scenario: First/last item navigation
    Given Carousel or interactive layout exists
    When User reaches first or last item
    Then Navigation controls work appropriately without error

  Scenario: Swipe and keyboard conflict resolution
    Given Device supports both swipe and keyboard
    When User uses both interaction methods
    Then Interaction remains consistent without conflicts
