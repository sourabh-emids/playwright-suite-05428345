Feature: Render How We Deliver section

  Scenario: Verify section renders with all content in sequence
    Given The page loads
    When The user views the How We Deliver section
    Then Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence

  Scenario: Verify section is accessible
    Given The How We Deliver section renders
    When Screen reader or keyboard user accesses the section
    Then All content is accessible with proper semantic structure

  Scenario: Verify required content fields not empty
    Given The How We Deliver section is configured
    When The section renders
    Then Required fields (title, body, CTA) are not empty

  Scenario: Verify heading hierarchy remains logical
    Given The How We Deliver section renders
    When The user inspects heading structure
    Then Heading levels follow logical hierarchy without skips where avoidable

  Scenario: Verify section renders without media
    Given How We Deliver section media is unavailable
    When The section renders
    Then Section renders with text content visible

  Scenario: Verify section renders with long copy
    Given How We Deliver section has long body copy
    When The section renders
    Then Content wraps appropriately without breaking layout
