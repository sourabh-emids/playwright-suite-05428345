"""Feature file for Issue 0048 - Inquiry Type values on contact form."""
Feature: Inquiry Type values on contact form

  Scenario: Select control contains approved options
    Given A user views the Inquiry Type select control
    When Options are examined
    Then Select contains: Services, Careers, Employment Verification, Media Request, Other

  Scenario: Valid choice required before submission
    Given User leaves Inquiry Type as placeholder
    When Form is submitted
    Then Submission is rejected; placeholder is not a valid choice

  Scenario: Values outside allowed enum rejected
    Given A tampered request submits an unknown Inquiry Type value
    When Server validates the submission
    Then Unknown value is rejected

  Scenario: Option removed while form cached handling
    Given An Inquiry Type option is removed from the system while user has cached form
    When User submits the form
    Then Server validates against current allowed values and rejects invalid selections
