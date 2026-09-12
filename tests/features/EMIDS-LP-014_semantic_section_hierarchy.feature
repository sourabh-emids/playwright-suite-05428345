Feature: Semantic section hierarchy

  Scenario: Exactly one page-level H1
    Given The entire landing page
    When Heading structure is analyzed
    Then Exactly one H1 element exists on the page

  Scenario: Logical heading levels for sections
    Given Section headings on the page
    When Heading levels are reviewed
    Then Subsequent section headings use logical levels (H2, H3, etc.) without skipping levels where avoidable

  Scenario: Landmarks are identifiable
    Given The page structure
    When Semantic landmarks are checked
    Then main, header, and footer landmarks are properly identified

  Scenario: Interactive text not styled as headings only
    Given Interactive elements
    When Elements styled as headings are reviewed
    Then Interactive text elements are not headings solely for styling purposes

  Scenario: CMS duplicate H1 scenario
    Given CMS editor introduces duplicate H1
    When Page renders
    Then QA process identifies the accessibility violation
