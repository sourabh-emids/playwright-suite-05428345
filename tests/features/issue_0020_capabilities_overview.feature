Feature: Render capabilities overview

  Scenario: All three capability groups visible
    Given User views Capabilities section
    When Checking group display
    Then AI, Engineering, and Platforms groups are all visible

  Scenario: Each group has corresponding content and actions
    Given User examines each capability group
    When Checking content and interactivity
    Then Each group contains summary content and relevant link/action

  Scenario: Group labels match navigation taxonomy
    Given User compares Capabilities section to header navigation
    When Checking label consistency
    Then Section labels 'AI', 'Engineering', 'Platforms' match navigation taxonomy exactly

  Scenario: Exactly three primary groups for this content version
    Given Current content version specification
    When Checking capability groups
    Then Exactly three primary groups display: AI, Engineering, Platforms

  Scenario: Missing group handled gracefully
    Given One capability group fails to load
    When Page renders
    Then Remaining groups display; missing group is logged

  Scenario: Mislabeled taxonomy detected
    Given CMS applies incorrect taxonomy label
    When Page renders
    Then QA catches mislabeling; correct taxonomy is enforced

  Scenario: Overflow content handled
    Given Capability content is extensive
    When Page renders at standard viewport
    Then Content does not overflow container boundaries
