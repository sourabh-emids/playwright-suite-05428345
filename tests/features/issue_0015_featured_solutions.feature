Feature: Render six featured solution items

  Scenario: All six entries present with correct numbering
    Given User views Featured Solutions section
    When Counting entries
    Then Six entries are visible with numbering 01 through 06

  Scenario: Six solutions have readable titles and supporting copy
    Given User views each solution entry
    When Checking content
    Then Each entry contains readable title and supporting summary text

  Scenario: Six solutions have intended destinations
    Given User clicks each solution entry
    When Navigation triggered
    Then Each solution links to its intended destination URL

  Scenario: Solution titles not blank
    Given User validates solution entries
    When Checking for empty titles
    Then All six solution titles are populated with non-empty text

  Scenario: Solution order controlled and preserved
    Given User views Featured Solutions
    When Checking order
    Then Solutions display in controlled order 01-06 as configured

  Scenario: Six entries rendered per content version
    Given Current content version specifies six solutions
    When Page renders
    Then Exactly six entries display: Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, and Agentic AI

  Scenario: One item unpublished handled gracefully
    Given One featured solution is unpublished
    When Page renders
    Then Unpublished item does not appear; five items display correctly

  Scenario: Duplicate order handled
    Given Configuration error causes duplicate order number
    When Page renders
    Then Items still render; duplicate order is detected and logged

  Scenario: Very long title handled
    Given Solution title is very long
    When Page renders at standard viewport
    Then Long title wraps gracefully without breaking card layout

  Scenario: Card media missing handled
    Given Solution card has no optional media configured
    When Page renders
    Then Card renders with text content; no broken image placeholder
