Feature: Resource-access handoff without false download implication

  Scenario: Download reaches resource detail flow
    Given eBook card with Download action
    When Download is selected
    Then User reaches resource detail/access flow, not direct file download

  Scenario: Implementation does not expose private asset endpoint
    Given Download implementation
    When Network requests are monitored
    Then Implementation does not fabricate or expose private asset endpoints

  Scenario: Gate clearly communicates required steps
    Given Gated resource access
    When Gate is encountered
    Then Required steps are clearly communicated to user

  Scenario: Only verified/published destinations used
    Given Resource destinations
    When URLs are verified
    Then Only verified and published destinations are used

  Scenario: Gated asset unavailable handling
    Given Edge case where gated asset unavailable
    When Access is attempted
    Then Appropriate error message is displayed
