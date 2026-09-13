Feature: See the model CTA functionality

  Scenario: CTA routes to FDCE detail page
    Given User is on How We Deliver section
    When User clicks 'See the model' CTA
    Then User is navigated to '/forward-deployed-context-engineering/'

  Scenario: CTA keyboard operable
    Given User is on How We Deliver section with keyboard focus
    When User focuses on 'See the model' CTA and presses Enter
    Then Navigation to FDCE page occurs

  Scenario: Accessible name describes action
    Given User uses screen reader
    When User encounters 'See the model' CTA
    Then Accessible name describes the action

  Scenario: CTA has visible hover state
    Given User hovers over 'See the model' CTA
    When Hover interaction occurs
    Then Visible hover state is displayed

  Scenario: CTA has visible focus state
    Given User tabs to 'See the model' CTA
    When Focus is received
    Then Visible focus state is displayed

  Scenario: Destination 404 handling
    Given User clicks 'See the model' CTA
    When FDCE destination returns 404
    Then User sees appropriate error page

  Scenario: No duplicate focus target
    Given Multiple CTAs exist on page
    When User navigates with keyboard
    Then Focus target is not duplicated
