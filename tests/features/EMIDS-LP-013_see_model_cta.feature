Feature: See the model CTA functionality

  Scenario: See the model CTA routes to FDCE page
    Given The See the model CTA in How We Deliver section
    When CTA is clicked
    Then User is navigated to /forward-deployed-context-engineering/

  Scenario: See the model CTA keyboard operable
    Given The See the model CTA
    When Activated via keyboard
    Then CTA responds and navigates on Enter or Space

  Scenario: CTA has descriptive accessible name
    Given See the model CTA
    When Accessibility is verified
    Then Accessible name describes the action

  Scenario: Destination is valid and accessible
    Given CTA destination URL
    When URL is tested
    Then URL is valid and does not return 404
