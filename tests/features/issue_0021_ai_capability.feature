"""Feature file for Issue 0021 - AI capability content rendering."""
Feature: AI capability content rendering

  Scenario: AI label and supporting content render
    Given A user views the Capabilities section
    When The AI capability panel/card loads
    Then AI label and supporting content are rendered

  Scenario: AI relevant link operable
    Given A user views the AI capability card
    When The user clicks the AI capability link
    Then The link navigates to the relevant AI capability page

  Scenario: AI capability title required
    Given A user or assistive technology examines the AI capability
    When The content is analyzed
    Then Title is present and not empty

  Scenario: AI capability URL valid
    Given A user examines the AI capability link
    When The URL is inspected
    Then URL is valid and resolves to the AI capability destination

  Scenario: Missing AI destination handling
    Given The AI capability destination page is unavailable
    When A user clicks the AI capability link
    Then Appropriate error handling occurs
