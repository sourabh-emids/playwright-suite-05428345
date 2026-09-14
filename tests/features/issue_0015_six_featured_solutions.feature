"""Feature: Six Featured Solution Items."""
Feature: Six Featured Solution Items

  @issue_0015
  Scenario: all_six_entries_present
    Given Featured Solutions section renders
    When Solution items are counted
    Then All six entries are present

  @issue_0015
  Scenario: numbering_01_to_06_correct
    Given Featured Solutions section renders
    When Numbering is checked
    Then Entries are numbered 01 through 06 in correct order

  @issue_0015
  Scenario: each_entry_readable_title_copy
    Given Each featured solution is inspected
    When Content is reviewed
    Then Each entry contains readable title and supporting copy

  @issue_0015
  Scenario: each_entry_intended_destination
    Given Featured solution items are reviewed
    When Links are checked
    Then Each entry has intended destination/action

  @issue_0015
  Scenario: titles_not_blank
    Given Featured solutions are configured
    When Titles are validated
    Then No titles are blank

  @issue_0015
  Scenario: order_controlled
    Given Featured solutions render
    When Order is compared to expected sequence
    Then Order follows configuration (01-06)

  @issue_0015
  Scenario: one_item_unpublished_handling
    Given One solution item is unpublished
    When Section renders
    Then Unpublished item is handled appropriately

  @issue_0015
  Scenario: very_long_title_handling
    Given Solution has very long title
    When Section renders at viewport
    Then Long title is handled gracefully without breaking layout

  @issue_0015
  Scenario: card_media_missing_handling
    Given Solution card media is missing
    When Card renders
    Then Card renders without breaking layout
