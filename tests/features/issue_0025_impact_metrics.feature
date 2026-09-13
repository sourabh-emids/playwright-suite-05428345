Feature: Impact proof metrics rendering

  Scenario: All four metrics visible as text
    Given User views Impact section
    When Page renders
    Then All four proof metrics are visible as text: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'

  Scenario: Values understandable without animation
    Given Count-up animation is disabled
    When User views Impact metrics
    Then Values remain understandable and display final meaningful values

  Scenario: Screen readers receive final values
    Given User uses screen reader
    When Screen reader encounters Impact metrics
    Then Final meaningful values are announced

  Scenario: Values and labels paired correctly
    Given Impact metrics render
    When User validates content
    Then Values and labels are managed as paired content

  Scenario: Currency symbol and plus sign preserved
    Given Impact metrics render
    When User views values with currency
    Then Currency symbols and plus signs are preserved where approved

  Scenario: Responsive metric grid
    Given User views Impact section at mobile width
    When Page renders
    Then Metric grid reflows responsively

  Scenario: Animation disabled accessibility
    Given User has prefers-reduced-motion enabled
    When Count-up animation is present
    Then Animation is disabled and final values display

  Scenario: Locale formatting handled
    Given User views Impact section in different locale
    When Values render
    Then Values remain understandable with appropriate locale formatting
