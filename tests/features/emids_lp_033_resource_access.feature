Feature: Implement resource-access handoff without falsely implying direct file download

  Scenario: Verify Download reaches resource detail/access flow
    Given eBook card with Download action renders
    When User clicks Download
    Then User is routed to resource detail/access experience, not assumed direct file download

  Scenario: Verify no fabricated private asset endpoint exposed
    Given User inspects network traffic during Download click
    When Download action is activated
    Then No private asset endpoint is exposed or fabricated in the request

  Scenario: Verify gate communicates required steps
    Given Resource is gated (requires form submission)
    When User clicks Download
    Then Gate clearly communicates required steps before access

  Scenario: Verify only verified destinations used
    Given Resource card is configured
    When Card renders
    Then Only verified/published destinations are used for card actions

  Scenario: Verify direct file URLs not assumed
    Given eBook resource is configured
    when Download action is implemented
    Then Implementation uses resource detail page, not assuming direct file URL structure

  Scenario: Verify gated asset unavailable handled
    Given Gated asset is unavailable
    When User completes access flow
    Then User-friendly error message displayed

  Scenario: Verify submission failure handled
    Given Resource access form submission fails
    When User submits form
    Then Clear error message displayed; user can retry

  Scenario: Verify popup blocked handled
    Given Popup blocker prevents downstream modal
    When Download action triggers popup
    Then Fallback navigation or notification displayed
