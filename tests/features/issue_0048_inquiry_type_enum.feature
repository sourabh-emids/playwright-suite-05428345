Feature: Support Inquiry Type enum values

  Scenario: Select control contains all approved options
    Given User views Inquiry Type field
    When Opening dropdown
    Then Options include: Services, Careers, Employment Verification, Media Request, Other

  Scenario: Valid choice required before submission
    Given User submits form without selecting Inquiry Type
    When Checking validation
    Then Form validation requires valid selection; placeholder 'Select...' not accepted

  Scenario: Native select or accessible combobox used
    Given User tests Inquiry Type accessibility
    When Navigating with keyboard
    Then Control is either native <select> or accessible custom combobox

  Scenario: Values outside allowed enum rejected
    Given Tampered request submits unknown value
    When Server processes
    Then Server rejects invalid enum value

  Scenario: Option removed while form cached handled
    Given Option removed from enum after user loaded form
    When User submits with previous option
    Then Server validates against current enum; rejects if option now invalid

  Scenario: Sanitized validation errors for unknown value
    Given Tampered request with unknown value
    When Server validates
    Then Error logged with sanitized details; no sensitive data exposed
