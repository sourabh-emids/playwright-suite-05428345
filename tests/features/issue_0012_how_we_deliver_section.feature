Feature: Render How We Deliver section

  Scenario: Section renders in intended sequence after hero
    Given User views the page
    When Scanning page structure
    Then How We Deliver section appears after hero section in document order

  Scenario: Section contains required content fields
    Given How We Deliver section is present
    When Checking required fields
    Then Section title, supporting explanation, visual/content elements, and CTA all render

  Scenario: Section is accessible
    Given User tests section accessibility
    When Navigating via screen reader or keyboard
    Then All content is accessible; heading hierarchy is logical

  Scenario: Required content fields cannot be empty
    Given CMS content is being loaded
    When Checking for empty required fields
    Then Section title, body, and CTA are populated; empty fields are not rendered

  Scenario: Heading hierarchy remains logical
    Given How We Deliver section has heading
    When Checking H tag sequence
    Then Headings follow logical order (H2 for section if H1 exists, etc.)

  Scenario: Missing media handled gracefully
    Given How We Deliver section visual is missing
    When Page renders
    Then Text content remains visible; section remains functional

  Scenario: Long copy handles without breaking layout
    Given Section body copy is very long
    When Page renders at standard viewport
    Then Layout accommodates content without horizontal overflow
