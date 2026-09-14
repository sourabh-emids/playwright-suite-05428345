Feature: Resource access handoff without false download implication

  Scenario: Download routes to resource detail flow not direct file
    Given User clicks Download on eBook card
    When Navigation occurs
    Then User navigates to resource detail/access flow page, not direct file URL

  Scenario: No fabricated private asset endpoint exposed
    Given User inspects network requests on Download click
    When Monitoring requests
    Then No direct file asset URL is exposed to client

  Scenario: Gate clearly communicates required steps
    Given Resource requires form/modal gate
    When User reaches gate page
    Then User sees clear communication about required steps to access resource

  Scenario: Only verified published destinations used
    Given CMS validation
    When Checking resource destinations
    Then All resource URLs are verified and point to published destinations

  Scenario: Direct file URLs not assumed
    Given Implementation approach review
    When Checking code for file URL patterns
    Then Code does not assume direct file URLs; uses detail page routes

  Scenario: Gated asset unavailable handled
    Given Gate asset fails to load
    When User reaches gate
    Then User sees appropriate unavailable message; form does not silently fail

  Scenario: Submission failure handled
    Given User submits access form
    When Submission fails
    Then User sees clear error message; can retry

  Scenario: Resource withdrawn handled
    Given User navigates to resource after withdrawal
    When Page loads
    Then Appropriate unavailable message displays

  Scenario: Popup blocked handled
    Given Popup approach used and blocked
    When User clicks action
    Then Content opens in main window or user notified about popup block
