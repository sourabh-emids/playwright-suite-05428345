Feature: Semantic section hierarchy
  # issue_0014

  Scenario: Exactly one H1 on page
    Given The page DOM is analyzed
    When Automated testing counts H1 elements
    Then Exactly one H1 element exists on the page

  Scenario: Logical heading hierarchy maintained
    Given All heading elements on the page
    When Automated testing validates heading levels
    Then Headings follow logical progression with no skipped levels (e.g., H1 to H3 without H2 is avoided)

  Scenario: Semantic landmarks identified
    Given The page structure is analyzed
    When Accessibility testing runs
    Then Main, header, and footer landmarks are identifiable by assistive technology

  Scenario: Interactive text not styled as headings
    Given Interactive elements exist on the page
    When The DOM is analyzed
    Then Interactive text elements are not using heading elements solely for styling purposes

  Scenario: Hidden headings not focusable
    Given Hidden content sections exist
    When Keyboard navigation testing runs
    Then Hidden headings are not focusable or announced by screen readers
