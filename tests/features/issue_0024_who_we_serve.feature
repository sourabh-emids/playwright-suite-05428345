"""Feature file for Issue 0024 - Five audience/industry entries rendering."""
Feature: Five audience/industry entries rendering

  Scenario: All five audiences visible
    Given A user views the Who We Serve section
    When The section loads
    Then All five audiences are visible

  Scenario: Each Explore action routes to canonical segment
    Given A user clicks the Explore action for an audience
    When The action is activated
    Then The user is routed to the canonical segment page

  Scenario: Keyboard and touch interactions work
    Given A user interacts with Who We Serve via keyboard and touch
    When The user navigates the section
    Then All interactions work on both keyboard and touch input

  Scenario: Exactly five current audiences
    Given A user analyzes the Who We Serve section
    When The content is counted
    Then Exactly five current audiences are displayed for this content version

  Scenario: One segment unavailable graceful handling
    Given One segment page is unavailable (e.g., HealthTech unpublished)
    When The section renders
    Then The unavailable segment is handled gracefully; remaining audiences display correctly

  Scenario: Tab state preserved after resize
    Given A user selects an audience tab and resizes the viewport
    When The viewport changes breakpoint
    Then Tab state is appropriately preserved or gracefully reset
