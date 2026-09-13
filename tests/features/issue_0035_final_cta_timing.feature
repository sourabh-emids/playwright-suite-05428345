Feature: 1 Day 2 Weeks 3 Months delivery message

  Scenario: All timing labels render
    Given User views Final CTA section
    When Page renders
    Then All timing labels render: '1 Day', '2 Weeks', '3 Months'

  Scenario: Labels in intended order
    Given User views timing labels
    When Labels display
    Then Labels appear in intended order (1 Day → 2 Weeks → 3 Months)

  Scenario: Readable to screen readers
    Given User uses screen reader
    When Screen reader encounters timing labels
    Then Timing labels are readable in logical order

  Scenario: Meaning not encoded in styling alone
    Given Timing labels render
    When CSS styling is disabled
    Then Meaning is conveyed through text, not visual styling alone

  Scenario: Explanatory labels included if configured
    Given Timing labels have explanatory labels
    When Page renders
    Then Explanatory labels display where configured

  Scenario: Mobile width wrapping
    Given User views Final CTA at mobile width
    When Page renders
    Then Timing labels wrap appropriately at mobile widths
