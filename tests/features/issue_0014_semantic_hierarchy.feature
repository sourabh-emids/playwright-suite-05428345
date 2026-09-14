Feature: Maintain semantic section hierarchy

  Scenario: Exactly one page-level H1 exists
    Given User checks page heading structure
    When Analyzing semantic HTML
    Then Exactly one H1 element is present on the page

  Scenario: Section headings use logical levels
    Given Page has multiple section headings
    When Checking heading hierarchy
    Then Headings increment logically (H2 for main sections, H3 for subsections)

  Scenario: Main header footer landmarks identifiable
    Given User runs accessibility audit
    When Checking landmark regions
    Then <header>, <main>, and <footer> landmarks are present and identifiable

  Scenario: No skipped heading levels
    Given Page heading structure
    When Checking for heading level gaps
    Then Heading levels follow logical sequence without skips (e.g., H1 to H3 without H2)

  Scenario: Interactive text not styled as headings only
    Given Page contains clickable text elements
    When Checking if styled headings are interactive
    Then Interactive elements are proper buttons/links, not styled heading elements

  Scenario: CMS duplicate H1 detection
    Given CMS editor introduces duplicate H1
    When Page renders
    Then QA testing catches and flags duplicate H1 before production

  Scenario: Hidden heading not focusable
    Given Page has visually hidden heading
    When User tabs through page
    Then Hidden heading is not included in focus order or announced by screen reader
