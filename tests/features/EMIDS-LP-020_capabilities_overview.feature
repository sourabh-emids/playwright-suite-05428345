Feature: Capabilities overview rendering

  Scenario: All three capability groups visible
    Given Capabilities section
    When Groups are inspected
    Then AI, Engineering, and Platforms groups are all visible

  Scenario: Each group has corresponding content/actions
    Given Each capability group
    When Content is reviewed
    Then Each group has corresponding summary and links/actions

  Scenario: Group labels match navigation taxonomy
    Given Capability group labels
    When Compared against navigation taxonomy
    Then Labels are consistent: AI, Engineering, Platforms

  Scenario: Responsive capability cards/panels
    Given Capabilities section at different viewport widths
    When Layout adapts
    Then Responsive cards/panels render correctly
