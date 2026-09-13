Feature: How We Deliver section rendering

  Scenario: Section heading renders in sequence
    Given User is on Emids homepage
    When Page renders below hero
    Then How We Deliver section heading appears in intended sequence after hero

  Scenario: Supporting explanation renders
    Given How We Deliver section is present
    When User views section content
    Then Supporting explanation text is present and readable

  Scenario: Visual elements render
    Given How We Deliver section is present
    When User views section
    Then Visual/content elements render appropriately

  Scenario: Section CTA renders
    Given How We Deliver section is present
    When User views section
    Then Section CTA is present and accessible

  Scenario: Section accessible
    Given User uses assistive technology
    When User navigates to How We Deliver section
    Then Section is accessible with proper semantic markup

  Scenario: Required content fields not empty
    Given How We Deliver section renders
    When User validates content
    Then Required content fields (title, body, CTA) are not empty

  Scenario: Heading hierarchy logical
    Given How We Deliver section is present
    When User checks heading structure
    Then Heading hierarchy follows logical order

  Scenario: Section responsive
    Given User views Emids homepage at mobile width
    When How We Deliver section renders
    Then Section reflows appropriately for mobile viewport
