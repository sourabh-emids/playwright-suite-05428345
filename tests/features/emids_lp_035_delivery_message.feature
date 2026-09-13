Feature: Render 1 Day · 2 Weeks · 3 Months delivery message

  Scenario: Verify all timing labels render in order
    Given Delivery message section renders
    When User views timing content
    Then Labels display in order: '1 Day', '2 Weeks', '3 Months'

  Scenario: Verify timing readable to screen readers
    Given Delivery message renders
    When Screen reader reads section
    Then All timing labels are announced in logical order with explanatory text if configured

  Scenario: Verify meaning not encoded via visual styling alone
    Given Delivery message renders
    When User views without CSS or uses screen reader
    Then Meaning is conveyed through text, not solely through visual styling

  Scenario: Verify missing explanation handled
    Given Explanatory labels are missing
    When Section renders
    Then Timing values render with available content; no broken placeholder

  Scenario: Verify wrapping at mobile widths
    Given Delivery message renders at mobile width
    When User views content
    Then Content wraps appropriately without horizontal overflow
