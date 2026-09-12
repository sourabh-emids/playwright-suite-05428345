"""Feature file for Issue 0012 - How We Deliver section rendering."""
Feature: How We Deliver section rendering

  Scenario: Section renders in intended sequence
    Given A user scrolls to the How We Deliver section
    When The section is in view
    Then Content renders in intended sequence: heading, supporting explanation, visual/content elements, and CTA

  Scenario: Section elements are accessible
    Given A user views the How We Deliver section with assistive technology
    When The user navigates the section
    Then All elements are accessible and heading hierarchy is logical

  Scenario: Required content fields not empty
    Given A user views the How We Deliver section
    When The section loads
    Then Required content fields (section title, copy, CTA) are not empty

  Scenario: Heading hierarchy maintained
    Given A user or assistive technology examines the page structure
    When The page HTML is analyzed
    Then Heading hierarchy (H1 > H2 > H3) remains logical

  Scenario: Section with missing media
    Given The section visual media is unavailable
    When The section renders
    Then Content renders without breaking; placeholder or fallback is provided
