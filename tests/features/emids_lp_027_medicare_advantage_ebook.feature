Feature: Display Medicare Advantage eBook card

  Scenario: Verify correct title for Medicare Advantage eBook
    Given Medicare Advantage eBook is configured
    When Insight card renders
    Then Card displays title 'Managing the Margin Reset in Medicare Advantage'

  Scenario: Verify eBook type label
    Given Medicare Advantage eBook card renders
    When User views card type
    Then Card is labeled with type 'eBook'

  Scenario: Verify imagery displays if available
    Given Medicare Advantage eBook has imagery configured
    When Card renders
    Then Card displays available image

  Scenario: Verify Download action displays
    Given Medicare Advantage eBook card renders
    When User views action
    Then Download action is displayed

  Scenario: Verify URL resolves to current detail page
    Given Medicare Advantage eBook is configured
    When User clicks Download action
    Then URL resolves to current detail/access page without 404

  Scenario: Verify resource removed handled
    Given Medicare Advantage resource is removed or gated
    When User clicks Download
    Then Appropriate error, gate, or redirect displayed
