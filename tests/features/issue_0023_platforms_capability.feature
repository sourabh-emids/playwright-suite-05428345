Feature: Render Platforms capability content

  Scenario: Platforms content renders with approved taxonomy
    Given User views Platforms capability card
    When Checking label
    Then Label uses approved taxonomy term (e.g., 'Platforms' or 'Provider Platforms' as approved)

  Scenario: Navigation and body naming consistent
    Given User compares header navigation to Platforms section body
    When Checking terminology consistency
    Then Navigation 'Platforms' matches section body label without inconsistent synonyms

  Scenario: Platforms card matches visual system
    Given User views Platforms card
    When Checking styling
    Then Card follows capability visual system

  Scenario: Platforms title required validation
    Given Content validation
    When Checking required fields
    Then Platforms title field is populated with approved label

  Scenario: Stale CMS content handled
    Given CMS has outdated Platforms content
    When Page renders
    Then Content governance workflow catches stale content before publishing
