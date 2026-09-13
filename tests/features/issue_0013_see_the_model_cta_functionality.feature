Feature: See the model CTA functionality
  # issue_0013

  Scenario: See the model CTA routes to FDCE
    Given The How We Deliver section is rendered
    When A user clicks the See the model CTA
    Then Navigation routes to the FDCE detail page at /forward-deployed-context-engineering/

  Scenario: See the model CTA is keyboard operable
    Given A user navigates using keyboard only
    When Focus reaches the CTA and Enter is pressed
    Then Navigation to the FDCE page occurs

  Scenario: See the model CTA has descriptive accessible name
    Given The CTA is rendered
    When Screen reader accesses the element
    Then The accessible name describes the action (e.g., 'See the model')

  Scenario: See the model destination returns 200
    Given The CTA is configured
    When Automated testing checks the destination URL
    Then The URL returns HTTP 200 status
