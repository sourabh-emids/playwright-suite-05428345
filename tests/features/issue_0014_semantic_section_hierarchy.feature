"""Feature: Semantic Section Hierarchy."""
Feature: Semantic Section Hierarchy

  @issue_0014
  Scenario: single_h1_on_page
    Given Page renders
    When H1 headings are counted
    Then Exactly one page-level H1 is present

  @issue_0014
  Scenario: logical_heading_levels
    Given Page heading structure is reviewed
    When Headings are inspected
    Then Subsequent section headings use logical levels (no skipped levels where avoidable)

  @issue_0014
  Scenario: semantic_landmarks_identifiable
    Given Page renders
    When Landmarks are inspected
    Then main, header, and footer landmarks are identifiable

  @issue_0014
  Scenario: interactive_text_not_heading_for_style
    Given Interactive elements exist
    When Heading structure is reviewed
    Then Interactive text is not styled as headings solely for visual effect

  @issue_0014
  Scenario: cms_duplicate_h1_handling
    Given CMS content contains duplicate H1
    When Page renders
    Then Duplicate H1 is prevented or resolved appropriately

  @issue_0014
  Scenario: hidden_heading_focus_handling
    Given Hidden content exists with headings
    When Focusable hidden content is revealed
    Then Hidden heading does not become unexpected focus target
