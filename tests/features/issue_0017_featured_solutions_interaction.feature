"""Feature file for Issue 0017 - Featured solution responsive interaction."""
Feature: Featured solution responsive interaction

  Scenario: Every solution reachable on keyboard
    Given A user navigates the Featured Solutions with keyboard
    When The user tabs through the section
    Then Every solution can be reached via keyboard navigation

  Scenario: Every solution reachable on touch
    Given A user views the site on a touch device
    When The user interacts with Featured Solutions
    Then Every solution can be reached via touch

  Scenario: No content hidden off-screen permanently
    Given A user views the Featured Solutions section
    When The user examines all content
    Then No content is permanently hidden off-screen; all solutions are accessible

  Scenario: Carousel controls have accessible labels
    Given A carousel or interactive rail is used
    When The user or assistive technology examines previous/next controls
    Then Controls have accessible labels describing their function

  Scenario: Autoplay respects reduced motion
    Given A user has prefers-reduced-motion enabled
    When The user views the Featured Solutions with autoplay carousel
    Then Autoplay does not prevent user control and respects reduced motion preference

  Scenario: Viewport resize mid-interaction
    Given A user is interacting with Featured Solutions and resizes the viewport
    When The viewport changes breakpoint
    Then Interaction state is preserved or gracefully adapted without breaking functionality

  Scenario: First/last item navigation
    Given A user navigates to the first item in a carousel
    When The user attempts to navigate to a previous item
    Then Navigation wraps appropriately or indicates boundary
