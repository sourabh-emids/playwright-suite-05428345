Feature: Six featured solution items rendering

  Scenario: All six entries are present with correct numbering
    Given Featured Solutions section
    When Solution items are counted and numbered
    Then Six entries exist numbered 01 through 06: Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, and Agentic AI

  Scenario: Each entry has title and supporting copy
    Given Each featured solution item
    When Content is reviewed
    Then Each entry contains readable title, supporting copy, and intended destination/action

  Scenario: Titles are not blank
    Given All featured solution titles
    When Titles are verified
    Then No titles are blank

  Scenario: Order is controlled
    Given Featured solutions display order
    When Items are inspected
    Then Items appear in controlled order 01-06

  Scenario: One item unpublished edge case
    Given Edge case where one solution is unpublished
    When Featured solutions render
    Then System handles gracefully with either placeholder or reduced count

  Scenario: Very long title handling
    Given A featured solution with very long title
    When Content renders
    Then Title is handled without breaking layout
