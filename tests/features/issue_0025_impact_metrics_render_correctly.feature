Feature: Impact metrics render correctly
  # issue_0025

  Scenario: All four metric value-label pairs visible as text
    Given The Impact section is rendered
    When Visual inspection runs
    Then All four metrics are displayed as text: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'

  Scenario: Values remain understandable without animation
    Given Animation is disabled or fails
    When The Impact section renders
    Then Final metric values are clearly readable and understandable

  Scenario: Screen readers receive meaningful final values
    Given Screen reader software accesses the Impact section
    When The content is announced
    Then Final numeric values and labels are communicated meaningfully

  Scenario: Values and labels managed as paired content
    Given The Impact metrics are managed in CMS
    When Automated testing validates data integrity
    Then Value and label pairs are maintained together correctly

  Scenario: Currency symbols and plus signs preserved
    Given The Impact metrics render
    When Content is inspected
    Then Currency symbols ($) and plus signs (+) are preserved where approved
