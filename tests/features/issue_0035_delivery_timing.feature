Feature: Render delivery timing message

  Scenario: All timing labels render in intended order
    Given User views final CTA section
    When Reading timing content
    Then 1 Day, 2 Weeks, and 3 Months display in that sequence

  Scenario: Timing labels understandable to screen readers
    Given Screen reader user navigates to timing section
    when Reading content
    Then All timing labels are announced in correct order with clear meaning

  Scenario: Meaning not encoded via visual styling alone
    Given Timing section styling review
    When Checking accessible presentation
    Then Timing meaning is conveyed through text, not purely visual differences

  Scenario: Explanatory labels present where configured
    Given Timing items have supporting explanations
    When Checking display
    Then Explanatory labels render alongside timing values

  Scenario: Missing explanation handled
    Given Timing item lacks explanation
    When Page renders
    Then Timing value still renders; missing explanation logged

  Scenario: Wrapping at mobile widths handled
    Given Narrow viewport
    When Timing content renders
    Then Content wraps gracefully without breaking layout
