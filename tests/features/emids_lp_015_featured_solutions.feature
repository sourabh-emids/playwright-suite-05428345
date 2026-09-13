Feature: Render six featured solution items

  Scenario: Verify all six entries are present
    Given The Featured Solutions section renders
    When The user counts solution items
    Then Exactly six solution entries are displayed

  Scenario: Verify numbering 01-06 is correct
    Given The Featured Solutions section renders
    When The user views the solution numbers
    Then Solutions are numbered 01, 02, 03, 04, 05, 06 in correct order

  Scenario: Verify each entry has readable title and summary
    Given Each featured solution item renders
    When The user views the solution cards/entries
    Then Each entry contains a readable title and supporting copy

  Scenario: Verify each entry has intended destination
    Given Featured solutions render
    When The user clicks or activates a solution entry
    Then Each entry routes to its intended destination or action URL

  Scenario: Verify titles are not blank
    Given Featured solutions are configured
    When The page renders
    Then No solution title is empty or blank

  Scenario: Verify order is controlled correctly
    Given Featured solutions are configured with specific order
    When The page renders
    Then Solutions display in configured order

  Scenario: Verify one item unpublished handled
    Given One of six solutions is unpublished
    When The section renders
    Then Only published solutions appear; section shows available items only

  Scenario: Verify very long title handled
    Given A featured solution has a very long title
    When The section renders
    Then Long title wraps or truncates gracefully without breaking layout

  Scenario: Verify card media missing handled
    Given A solution card has no media configured
    When The section renders
    Then Card renders without media placeholder or uses text-only layout
