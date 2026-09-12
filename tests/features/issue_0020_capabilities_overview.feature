"""Feature file for Issue 0020 - Capabilities overview rendering."""
Feature: Capabilities overview rendering

  Scenario: All three capability groups visible
    Given A user views the Capabilities section
    When The section loads
    Then All three groups (AI, Engineering, Platforms) are visible with corresponding content and actions

  Scenario: Group labels match navigation taxonomy
    Given A user compares capabilities section to header navigation
    When The labels are compared
    Then Group labels match the navigation taxonomy exactly

  Scenario: Three primary groups for this content version
    Given A user views the Capabilities section
    When The section content is analyzed
    Then Exactly three primary capability groups are displayed

  Scenario: Responsive capability cards/panels
    Given A user views the Capabilities section at various viewport widths
    When The viewport changes
    Then Capability cards/panels reflow responsively without content loss

  Scenario: Group missing handling
    Given One capability group is missing from the data
    When The section renders
    Then The section renders with remaining groups; missing group does not cause errors
