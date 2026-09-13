Feature: Capabilities overview rendering

  Scenario: All three groups visible
    Given User views Capabilities section
    When Page renders
    Then All three capability groups (AI, Engineering, Platforms) are visible

  Scenario: Each group has corresponding content/actions
    Given Capabilities section renders
    When User views each capability group
    Then Each group has corresponding content and actions

  Scenario: Group labels match navigation taxonomy
    Given Capabilities section renders
    When User compares section labels to navigation
    Then Group labels (AI, Engineering, Platforms) match navigation taxonomy

  Scenario: Three primary groups required
    Given Capabilities section renders
    When User counts primary groups
    Then Exactly three primary groups are present for this content version

  Scenario: Responsive capability cards/panels
    Given User views Capabilities section at mobile width
    When Page renders
    Then Section uses responsive capability cards/panels

  Scenario: Group missing handling
    Given One capability group is missing from CMS
    When Page renders
    Then Remaining groups display correctly or appropriate fallback shows
