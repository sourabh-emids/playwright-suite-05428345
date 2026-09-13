Feature: Provide See the model CTA

  Scenario: Verify See the model CTA routes to FDCE page
    Given The See the model CTA is rendered in How We Deliver section
    When The user clicks the CTA
    Then The CTA routes to '/forward-deployed-context-engineering/'

  Scenario: Verify CTA is keyboard operable
    Given The See the model CTA is rendered
    When The user focuses on CTA via keyboard
    Then The CTA can be activated using Enter or Space key

  Scenario: Verify accessible name describes action
    Given The See the model CTA is rendered
    When Screen reader reads the CTA
    Then Accessible name clearly describes the action 'See the model'

  Scenario: Verify visible hover and focus states
    Given The See the model CTA is rendered
    When User hovers or focuses on the CTA
    Then Visual hover/focus states are visible

  Scenario: Verify destination 404 handled
    Given FDCE detail page returns 404
    When User clicks See the model CTA
    Then Page displays appropriate error without breaking navigation
