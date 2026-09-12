"""Feature file for Issue 0025 - Impact proof metrics rendering."""
Feature: Impact proof metrics rendering

  Scenario: All four value/label pairs visible as text
    Given A user views the Impact section
    When The section loads
    Then All four metrics are visible as text

  Scenario: Values understandable without animation
    Given A user views the Impact section with animations disabled
    When The metrics are displayed
    Then Values remain understandable; count-up animation does not obscure final values

  Scenario: Screen readers receive meaningful values
    Given A user uses a screen reader to navigate the Impact section
    When The screen reader encounters the metrics
    Then Final meaningful values are announced

  Scenario: Values and labels as paired content
    Given A user or assistive technology examines the metrics
    When The content is analyzed
    Then Values and labels are managed as paired content with correct associations

  Scenario: Currency symbol and plus sign preserved
    Given A user views the impact metrics
    When The values are displayed
    Then Currency symbols ($) and plus signs (+) are preserved where approved
