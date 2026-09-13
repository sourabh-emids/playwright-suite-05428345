Feature: Semantic section hierarchy

  Scenario: Exactly one page-level H1
    Given User views Emids homepage
    When User counts H1 elements
    Then Exactly one H1 element exists on the page

  Scenario: Subsequent headings use logical levels
    Given Page has multiple sections
    When User reviews heading hierarchy
    Then Section headings use logical levels (H2, H3, etc.) without skipping levels where avoidable

  Scenario: Main landmark identifiable
    Given User views Emids homepage
    When User identifies main landmark
    Then Main landmark is identifiable using <main> element

  Scenario: Header landmark identifiable
    Given User views Emids homepage
    When User identifies header landmark
    Then Header landmark is identifiable using <header> element

  Scenario: Footer landmark identifiable
    Given User views Emids homepage
    When User identifies footer landmark
    Then Footer landmark is identifiable using <footer> element

  Scenario: No skipped heading levels where avoidable
    Given User reviews heading structure
    When Headings are analyzed
    Then No heading levels are skipped (e.g., H1 to H3) where avoidable

  Scenario: Interactive text not headings solely for styling
    Given User views interactive elements
    When User analyzes heading elements
    Then Interactive text elements are not styled as headings solely for visual styling purposes

  Scenario: CMS duplicate H1 prevention
    Given CMS content is managed
    When Page renders
    Then No duplicate H1 elements are introduced by CMS

  Scenario: Hidden heading not focusable
    Given Hidden/sr-only headings exist
    When User navigates with keyboard
    Then Hidden headings are not accidentally focusable
