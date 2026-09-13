Feature: Final conversion banner render
  # issue_0034

  Scenario: Banner appears before footer
    Given The page has fully loaded
    When Visual inspection confirms section order
    Then The final conversion banner appears after main content and before the footer

  Scenario: Primary action is clear and keyboard operable
    Given The final conversion banner is rendered
    When Keyboard navigation testing runs
    Then The primary CTA is clearly identifiable and keyboard accessible

  Scenario: Supporting content is readable
    Given The final conversion banner is rendered
    When Visual inspection runs
    Then Timing/message content is readable and understandable

  Scenario: Required message and CTA fields are present
    Given The final CTA section is managed by CMS
    When Required field validation runs
    Then Required message and CTA fields are present and non-empty

  Scenario: High contrast closing CTA section
    Given The final conversion banner is rendered
    When Color contrast testing runs
    Then Text and background meet WCAG AA contrast requirements

---
Feature: Delivery message render
  # issue_0035

  Scenario: All timing labels render in intended order
    Given The final conversion section is rendered
    When Visual inspection confirms timing content
    Then Labels display in order: '1 Day', '2 Weeks', '3 Months'

  Scenario: Timing labels readable by screen readers
    Given The timing message is rendered
    When Screen reader testing runs
    Then All timing labels are announced correctly

  Scenario: Meaning not encoded via visual styling alone
    Given The timing message is rendered
    When Content is analyzed without visual styling
    Then Meaning is conveyed through text content, not visual styling alone

  Scenario: Timing message displays without wrapping issues at mobile
    Given The final conversion section is rendered at mobile width
    When Visual inspection runs
    Then Timing labels display correctly without problematic wrapping
