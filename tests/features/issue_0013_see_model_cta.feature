Feature: Provide See the model CTA

  Scenario: See the model CTA routes to FDCE detail page
    Given User clicks the 'See the model' CTA
    When Navigation occurs
    Then User is navigated to /forward-deployed-context-engineering/

  Scenario: See the model CTA is keyboard operable
    Given User focuses on the CTA via Tab
    When User presses Enter
    Then Navigation to FDCE page is triggered

  Scenario: CTA has descriptive accessible name
    Given User inspects CTA accessibility
    When Checking accessible name
    Then Accessible name describes the action 'See the model'

  Scenario: CTA visible hover and focus states
    Given User hovers or focuses on CTA
    When Checking visual feedback
    Then Visible hover and focus states are present

  Scenario: FDCE destination 404 handled
    Given FDCE page returns 404
    When User clicks See the model CTA
    Then Error page displays appropriately

  Scenario: CTA not duplicate focus target
    Given Multiple CTAs exist in section
    When User tabs through section
    Then Each CTA is individually focusable; no duplicate tab stops
