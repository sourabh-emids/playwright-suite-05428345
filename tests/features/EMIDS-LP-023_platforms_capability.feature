Feature: Platforms capability content rendering

  Scenario: Platforms content renders
    Given Platforms capability card/panel
    When Content is verified
    Then Platforms content is present

  Scenario: Labels use approved taxonomy consistently
    Given Platforms label in navigation and body copy
    When Labels are compared
    Then Labels use approved taxonomy consistently (e.g., 'Platforms' not variant synonyms)

  Scenario: Navigation/body naming consistency
    Given Content governance check
    When Navigation and body copy labels are audited
    Then Inconsistent synonyms are prevented unless intentionally approved

  Scenario: Stale CMS content detection
    Given CMS content update scenario
    When Content becomes outdated
    Then Publishing workflow logs content validation issues
