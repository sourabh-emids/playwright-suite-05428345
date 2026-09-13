Feature: Hero CTA routes to FDCE experience

  Scenario: Hero CTA resolves to FDCE page
    Given User is on Emids homepage viewing hero
    When User clicks the hero CTA
    Then User is navigated to '/forward-deployed-context-engineering/'

  Scenario: CTA URL is HTTPS and canonical
    Given User inspects hero CTA URL
    When User examines href attribute
    Then URL uses HTTPS protocol and is canonical

  Scenario: CTA routes with new tab behavior
    Given User right-clicks hero CTA
    When User selects Open in New Tab
    Then FDCE page opens in new tab

  Scenario: Destination unavailable handling
    Given User clicks hero CTA
    When FDCE destination is unavailable (404/503)
    Then User sees appropriate error page
