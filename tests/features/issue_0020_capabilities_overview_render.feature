Feature: Capabilities overview render
  # issue_0020

  Scenario: All three capability groups visible
    Given The Capabilities section is rendered
    When Visual inspection runs
    Then Three groups are visible: AI, Engineering, and Platforms

  Scenario: Each group has corresponding content
    Given The Capabilities section is rendered
    When Each capability group is analyzed
    Then Each group contains summary text and/or links/media

  Scenario: Group labels match navigation taxonomy
    Given The Capabilities section is rendered
    When Labels are compared to header navigation
    Then Group labels (AI, Engineering, Platforms) match the navigation taxonomy exactly

  Scenario: Responsive capability cards layout correctly
    Given The Capabilities section is rendered
    When Viewport is resized across breakpoints
    Then Capability cards/panels reflow appropriately without breaking layout
