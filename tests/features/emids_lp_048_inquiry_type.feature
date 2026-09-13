Feature: Support Inquiry Type values on contact form

  Scenario: Verify select contains approved options
    Given Inquiry Type field renders
    When User opens dropdown
    Then Options include: Services, Careers, Employment Verification, Media Request, Other

  Scenario: Verify valid choice required before submission
    Given Inquiry Type is marked required
    When User attempts to submit without selecting
    Then Validation error displayed; placeholder 'Select...' not accepted as valid choice

  Scenario: Verify unknown values rejected
    Given Form receives tampered request with unknown Inquiry Type
    When Server validates submission
    Then Unknown values outside allowed enum are rejected

  Scenario: Verify native select or accessible combobox
    Given Inquiry Type field renders
    When User interacts via keyboard
    Then Field is usable with native select behavior or accessible custom combobox

  Scenario: Verify option removed while form cached handled
    Given Form is cached but one option has been removed from system
    When User submits with removed option
    Then Server validates and rejects; user sees current options

  Scenario: Verify tampered request handled
    Given User manipulates form DOM to submit unknown value
    When Server receives submission
    Then Server validates against allowed enum; rejects tampered values
