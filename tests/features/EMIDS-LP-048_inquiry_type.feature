Feature: Inquiry Type values on contact form

  Scenario: Select control contains approved options
    Given Inquiry Type field
    When Options are inspected
    Then Options include: Services, Careers, Employment Verification, Media Request, Other

  Scenario: Valid choice required before submission
    Given Inquiry Type if marked required
    When Placeholder or no selection made
    Then Submission is prevented

  Scenario: Placeholder not valid submitted choice
    Given Inquiry Type with 'Select...' placeholder
    When Submission is attempted with placeholder
    Then Submission is rejected

  Scenario: Values outside enum rejected
    Given Tampered form submission
    When Unknown inquiry type value submitted
    Then Value outside allowed enum is rejected
