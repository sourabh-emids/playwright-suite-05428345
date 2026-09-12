"""Feature file for Issue 0015 - Six featured solution items rendering."""
Feature: Six featured solution items rendering

  Scenario: All six entries present
    Given A user views the Featured Solutions section
    When The section loads
    Then All six entries are present

  Scenario: Numbering 01-06 is correct
    Given A user views the Featured Solutions section
    When The solution entries are displayed
    Then Each entry is numbered 01 through 06 correctly in order

  Scenario: Each entry has title and summary
    Given A user views any featured solution card
    When The card is examined
    Then Each entry contains a readable title and supporting copy

  Scenario: Each entry has intended destination
    Given A user clicks on a featured solution
    When The solution link is activated
    Then The user is routed to the intended destination or action

  Scenario: Titles are not blank
    Given A user views the Featured Solutions section
    When The solution entries are examined
    Then No entry has a blank title

  Scenario: One item unpublished handling
    Given One featured solution is unpublished
    When The section renders
    Then The unpublished item is excluded or handled gracefully

  Scenario: Very long title handling
    Given A solution title exceeds expected character count
    When The card renders
    Then The title is handled gracefully (wrapped or truncated without breaking layout)

  Scenario: Card media missing handling
    Given A featured solution card has no media configured
    When The card renders
    Then The card renders without broken image placeholders; text content remains complete
