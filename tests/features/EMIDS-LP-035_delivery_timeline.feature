Feature: Delivery timeline message rendering

  Scenario: All timing labels render in intended order
    Given Delivery/timing message section
    When Content is inspected
    Then 1 Day, 2 Weeks, 3 Months render in correct order

  Scenario: Timing labels understandable to screen readers
    Given Timing labels
    When Read by screen reader
    Then Labels are understandable without visual styling context

  Scenario: Meaning not encoded by visual styling alone
    Given Timeline message content
    When Styling is analyzed
    Then Meaning is not conveyed through visual styling alone

  Scenario: Mobile width wrapping
    Given Timeline at mobile widths
    When Content wraps
    Then Content remains readable and properly associated
