Feature: Route hero CTA to FDCE experience

  Scenario: Hero CTA resolves to FDCE page
    Given User clicks hero CTA
    When Navigation occurs
    Then User lands on canonical FDCE URL /forward-deployed-context-engineering/

  Scenario: FDCE URL uses HTTPS protocol
    Given User inspects hero CTA URL
    When Checking protocol
    Then URL uses HTTPS secure protocol

  Scenario: Hero CTA preserves browser navigation behavior
    Given User right-clicks hero CTA
    When User selects Open in New Tab
    Then Page opens in new tab as expected; standard navigation behaviors preserved

  Scenario: FDCE destination unavailable handled gracefully
    Given FDCE destination page returns 404
    When User clicks hero CTA
    Then Appropriate error handling occurs without page crash

  Scenario: Hero CTA destination redirect handled
    Given FDCE destination has redirect configured
    When User clicks hero CTA
    Then User lands on final destination URL with redirect completed
