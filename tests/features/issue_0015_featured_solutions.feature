Feature: Six featured solution items rendering

  Scenario: All six entries present
    Given User is on Emids homepage
    When User views Featured Solutions section
    Then All six solution entries are present

  Scenario: Numbering 01-06 correct
    Given Featured Solutions section renders
    When User views solution numbers
    Then Solutions are numbered correctly from 01 to 06

  Scenario: Each entry has readable title
    Given Featured Solutions section renders
    When User views each solution entry
    Then Each entry contains a readable title (Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, Agentic AI)

  Scenario: Each entry has supporting copy
    Given Featured Solutions section renders
    When User views each solution entry
    Then Each entry contains supporting copy

  Scenario: Each entry has intended destination
    Given Featured Solutions section renders
    When User views each solution entry
    Then Each entry has an intended destination URL or action

  Scenario: Titles not blank
    Given Featured Solutions section renders
    When User validates content
    Then No solution titles are blank

  Scenario: Order controlled
    Given Featured Solutions section renders
    When User views solution order
    Then Solutions appear in controlled order (01-06)

  Scenario: Responsive layout without hiding content
    Given User views Featured Solutions at mobile width
    When Page renders
    Then Responsive layout (cards/list/rail/stacked) retains all content

  Scenario: One item unpublished handling
    Given One solution is unpublished in CMS
    When Page renders
    Then Either all six entries display correctly or appropriate fallback displays

  Scenario: Very long title handling
    Given Solution has very long title
    When Page renders at narrow viewport
    Then Title text wraps appropriately without breaking layout
