Feature: How We Deliver section render
  # issue_0012

  Scenario: Section renders in intended sequence
    Given The page has loaded
    When Visual inspection confirms section order
    Then The How We Deliver section appears after the hero and before other content, containing title, copy, visual, and CTA

  Scenario: Section content is accessible
    Given The How We Deliver section is rendered
    When Accessibility testing runs
    Then All content is readable by assistive technology with proper semantic structure

  Scenario: Required fields cannot be empty
    Given The section is managed by CMS
    When Automated testing validates required fields
    Then Section title, body copy, and CTA are present and non-empty

  Scenario: Heading hierarchy remains logical
    Given The page section hierarchy is analyzed
    When Automated accessibility testing runs
    Then Heading levels follow logical progression (H1 > H2 > H3)
