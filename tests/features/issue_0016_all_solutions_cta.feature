"""Feature: All Solutions CTA Rendering."""
Feature: All Solutions CTA Rendering

  @issue_0016
  Scenario: all_solutions_cta_visible
    Given Featured Solutions section renders
    When Section is reviewed
    Then All Solutions CTA is visible after or within the section

  @issue_0016
  Scenario: all_solutions_cta_routes_correctly
    Given User clicks All Solutions CTA
    When Navigation completes
    Then CTA routes to solutions portfolio at /solutions/

  @issue_0016
  Scenario: all_solutions_cta_canonical_url
    Given All Solutions CTA is configured
    When URL is validated
    Then URL is canonical

  @issue_0016
  Scenario: portfolio_page_unavailable
    Given Portfolio page at /solutions/ is unavailable
    When User clicks All Solutions CTA
    Then User sees appropriate error handling
