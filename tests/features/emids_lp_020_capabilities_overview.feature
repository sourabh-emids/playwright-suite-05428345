Feature: Render capabilities overview

  Scenario: Verify all three groups visible
    Given Capabilities section renders
    When User views the section
    Then AI, Engineering, and Platforms capability groups are visible

  Scenario: Verify each group has corresponding content/actions
    Given Capability groups render
    When User views each group
    Then Each group displays summary, links, and optional media as configured

  Scenario: Verify group labels match navigation taxonomy
    Given Capabilities section renders
    When User compares to header navigation
    Then Group labels (AI, Engineering, Platforms) match navigation taxonomy exactly

  Scenario: Verify exactly three primary groups
    Given Capabilities section renders
    When User counts primary groups
    Then Exactly three primary groups are configured for this content version

  Scenario: Verify missing group handled
    Given One capability group is missing from configuration
    When Section renders
    Then Remaining groups render; section does not break

  Scenario: Verify overflow handled gracefully
    Given Capability cards have long content
    When Section renders at narrow viewport
    Then Content reflows without breaking layout or hiding content
