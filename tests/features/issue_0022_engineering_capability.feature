"""Feature file for Issue 0022 - Engineering capability content rendering."""
Feature: Engineering capability content rendering

  Scenario: Engineering label and supporting content render
    Given A user views the Capabilities section
    When The Engineering capability panel/card loads
    Then Engineering label and supporting content are rendered

  Scenario: Engineering relevant link operable
    Given A user views the Engineering capability card
    When The user clicks the Engineering capability link
    Then The link navigates to the relevant Engineering capability page

  Scenario: Engineering capability title required
    Given A user or assistive technology examines the Engineering capability
    When The content is analyzed
    Then Title is present and not empty

  Scenario: Engineering capability URL valid
    Given A user examines the Engineering capability link
    When The URL is inspected
    Then URL is valid and resolves to the Engineering capability destination
