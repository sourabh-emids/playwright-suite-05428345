Feature: Hero CTA routes to FDCE experience

  Scenario: Hero CTA resolves to FDCE page
    Given The hero CTA button
    When Inspected for destination
    Then CTA routes to /forward-deployed-context-engineering/

  Scenario: Hero CTA preserves browser navigation behavior
    Given Hero CTA is clicked
    When Navigation occurs
    Then Standard browser navigation behavior is preserved (back button works, referrer is set)

  Scenario: Hero CTA URL is HTTPS and canonical
    Given Hero CTA destination
    When URL is verified
    Then URL uses HTTPS and is canonical

  Scenario: Hero CTA opens in new tab
    Given User right-clicks hero CTA
    When User selects 'Open in new tab'
    Then FDCE page opens in new tab
