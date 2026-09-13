Feature: Render Impact proof metrics

  Scenario: Verify all four value-label pairs visible as text
    Given Impact section renders
    When User views the section
    Then All four metrics display as visible text: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'

  Scenario: Verify values understandable without animation
    Given Metrics display with count-up animation
    When User views values or uses screen reader
    Then Final meaningful values are displayed and announced

  Scenario: Verify screen readers receive final values
    Given Metrics render with animation
    When Screen reader reads the section
    Then Screen reader receives final meaningful values, not intermediate animation states

  Scenario: Verify currency symbol and plus sign preserved
    Given Metrics are configured with symbols
    When Section renders
    Then Currency symbols ($) and plus signs (+) are preserved as approved

  Scenario: Verify animation disabled handled
    Given User prefers reduced motion or animation disabled
    When Impact section renders
    Then Final values display immediately without animation

  Scenario: Verify CMS field missing handled
    Given A metric value or label is missing from CMS
    When Section renders
    Then Missing field displays placeholder or section renders without broken content
