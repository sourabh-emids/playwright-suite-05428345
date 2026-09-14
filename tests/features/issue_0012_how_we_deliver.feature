"""Feature: How We Deliver Section Rendering."""
Feature: How We Deliver Section Rendering

  @issue_0012
  Scenario: section_renders_intended_sequence
    Given How We Deliver section is configured
    When Page renders
    Then Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence

  @issue_0012
  Scenario: section_accessible
    Given How We Deliver section renders
    When Accessibility is checked
    Then All content elements are accessible

  @issue_0012
  Scenario: section_required_fields_nonempty
    Given How We Deliver content is configured
    When Required fields are validated
    Then Required content fields (title, body, CTA) are non-empty

  @issue_0012
  Scenario: heading_hierarchy_logical
    Given Page heading structure is reviewed
    When Headings follow logical hierarchy from H1 through subsequent levels
    Then Heading hierarchy remains logical (H1 > H2 > H3)

  @issue_0012
  Scenario: missing_media_handling
    Given Visual media is not available
    When Section renders
    Then Section renders appropriately without breaking layout

  @issue_0012
  Scenario: long_copy_handling
    Given Section has unusually long copy
    When Section renders at viewport
    Then Content reflows without breaking layout
