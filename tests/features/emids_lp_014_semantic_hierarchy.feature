Feature: Maintain semantic section hierarchy

  Scenario: Verify exactly one page-level H1
    Given The homepage renders
    When The user counts H1 elements
    Then Exactly one H1 element exists on the page

  Scenario: Verify subsequent headings use logical levels
    Given The page contains multiple section headings
    When The user inspects heading hierarchy
    Then H2, H3, etc. follow logical progression without skipping levels where avoidable

  Scenario: Verify main, header, footer landmarks identifiable
    Given The homepage renders
    When The user or assistive technology inspects page structure
    Then Main, header, and footer regions have identifiable landmark roles

  Scenario: Verify no headings used for styling alone
    Given The page has interactive text elements
    When The user inspects heading elements
    Then Interactive text is not marked as headings solely for visual styling purposes

  Scenario: Verify duplicate H1 from CMS rejected
    Given CMS editor introduces duplicate H1 content
    When The page renders
    Then Only one H1 is rendered; additional content uses proper heading levels

  Scenario: Verify hidden heading not focusable
    Given A heading exists but is visually hidden
    When User navigates via keyboard
    Then Hidden heading is not focusable or announced as navigation target
