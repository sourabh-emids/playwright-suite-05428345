"""Feature file for Issue 0014 - Semantic section hierarchy maintenance."""
Feature: Semantic section hierarchy maintenance

  Scenario: Exactly one page-level H1
    Given A user or search engine examines the page HTML
    When The page structure is analyzed
    Then Exactly one H1 element exists on the page

  Scenario: Subsequent headings use logical levels
    Given A user examines the heading structure
    When The heading hierarchy is analyzed
    Then Section headings use logical levels (H2, H3, etc.) without skipping levels

  Scenario: Main/header/footer landmarks identifiable
    Given A user using assistive technology navigates the page
    When The user invokes landmark navigation
    Then Main, header, and footer landmarks are identifiable

  Scenario: Interactive text not headings for styling only
    Given A user examines the page HTML
    When Interactive elements are found
    Then Interactive text is not styled as headings solely for visual styling purposes

  Scenario: CMS editor duplicate H1 detection
    Given A CMS editor accidentally introduces a duplicate H1
    When The page is rendered
    Then QA testing detects the duplicate H1 accessibility violation
