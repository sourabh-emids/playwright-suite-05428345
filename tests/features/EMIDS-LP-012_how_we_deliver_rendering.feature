Feature: How We Deliver section rendering

  Scenario: Section renders in intended sequence
    Given The homepage structure
    When Content order is verified
    Then How We Deliver section appears after hero with section heading, explanation, visual/content elements, and CTA in sequence

  Scenario: Section content is accessible
    Given How We Deliver section
    When Accessibility is checked
    Then All content is accessible to assistive technologies

  Scenario: Required content fields not empty
    Given Section heading, copy, visual, and CTA
    When Content is inspected
    Then All required content fields are populated

  Scenario: Heading hierarchy is logical
    Given Section heading levels
    When Heading structure is verified
    Then Headings follow logical hierarchy without skips

  Scenario: Section without CTA
    Given Edge case where CTA fails to load
    When Section renders
    Then Section remains functional with remaining content
