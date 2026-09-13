Feature: Render Platforms capability content

  Scenario: Verify Platforms content renders
    Given Platforms capability is configured
    When The capabilities section renders
    Then Platforms label and supporting content display correctly

  Scenario: Verify labels use approved taxonomy consistently
    Given Platforms capability renders
    When User compares navigation and body copy labels
    Then Labels use approved taxonomy consistently (e.g., 'Platforms' not variants like 'Provider Platforms')

  Scenario: Verify navigation and body naming match
    Given Platforms capability is in both header navigation and body copy
    When User compares naming
    Then Navigation label and body copy label are consistent

  Scenario: Verify intentionally approved synonyms handled
    Given Content governance approves intentional synonym
    When Section renders
    Then Approved synonym displays where intentionally configured

  Scenario: Verify stale CMS content handled
    Given CMS contains outdated taxonomy for Platforms
    When Section renders
    Then Current approved taxonomy is used; stale content flagged in publishing workflow
