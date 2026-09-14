Feature: Render Impact proof metrics

  Scenario: All four metric value-label pairs visible
    Given User views Impact section
    When Checking metrics display
    Then All four metrics visible: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, and 450+ Platforms Launched

  Scenario: Metrics visible as text not just animation
    Given User or screen reader views metrics
    When Checking text availability
    Then Final metric values are rendered as visible text

  Scenario: Screen readers receive meaningful values
    Given Screen reader user navigates to metrics
    When Reading content
    Then Screen reader announces metric values and labels correctly

  Scenario: Currency symbols and plus signs preserved
    Given User views metric values
    When Checking character display
    Then Symbols like '$' and '+' are displayed where approved

  Scenario: Metrics as paired content validated
    Given CMS content validation
    When Checking metric data
    Then Value and label are managed as paired content; unpaired data is flagged

  Scenario: Count-up animation does not obscure final values
    Given User cannot see animation due to prefers-reduced-motion
    When Page renders
    Then Final metric values are visible as static text

  Scenario: CMS field missing handled
    Given One metric field is missing in CMS
    When Page renders
    Then Missing metric is logged; existing metrics display correctly

  Scenario: Locale formatting handled
    Given User views metrics in different locale
    when Checking number formatting
    Then Numbers remain understandable; locale-specific formatting applied where appropriate
