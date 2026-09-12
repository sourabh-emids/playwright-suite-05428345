Feature: Impact proof metrics rendering

  Scenario: All four metrics visible as text
    Given Impact section
    When Metrics are inspected
    Then All four values visible: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, 450+ Platforms Launched

  Scenario: Values understandable without animation
    Given Metrics with optional count-up animation
    When Animation is disabled or skipped
    Then Final meaningful values remain understandable

  Scenario: Screen readers receive final values
    Given Screen reader testing
    When Impact section is read
    Then Screen readers receive final meaningful values

  Scenario: Currency and plus signs preserved
    Given Metric values with special characters
    When Values are rendered
    Then Currency symbols ($) and plus signs (+) are preserved where approved

  Scenario: Values and labels managed as paired content
    Given CMS content management
    When Values are updated
    Then Value and label pairs remain properly associated
