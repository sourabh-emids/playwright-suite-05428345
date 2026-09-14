"""Feature: Hero CTA Routes to FDCE Experience."""
Feature: Hero CTA Routes to FDCE Experience

  @issue_0010
  Scenario: hero_cta_resolves_to_fdce
    Given User clicks hero CTA
    When Navigation completes
    Then CTA resolves to canonical FDCE page at /forward-deployed-context-engineering/

  @issue_0010
  Scenario: hero_cta_https_canonical
    Given Hero CTA is configured
    When URL is validated
    Then URL is HTTPS and canonical

  @issue_0010
  Scenario: hero_cta_navigation_behavior
    Given User clicks hero CTA
    When Navigation occurs
    Then Browser navigation behaves as expected (history entry created)

  @issue_0010
  Scenario: hero_cta_new_tab
    Given User opens hero CTA in new tab
    When New tab loads
    Then Destination page loads correctly

  @issue_0010
  Scenario: fdce_destination_unavailable
    Given FDCE destination page is unavailable
    When User clicks hero CTA
    Then User sees appropriate error or redirect
