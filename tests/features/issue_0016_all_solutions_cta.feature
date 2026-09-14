Feature: Provide All Solutions CTA

  Scenario: All Solutions CTA visible within section
    Given User views Featured Solutions section
    When Locating CTA
    Then All Solutions CTA is visible either after or within the section

  Scenario: All Solutions CTA routes to portfolio
    Given User clicks All Solutions CTA
    When Navigation occurs
    Then User navigates to /solutions/

  Scenario: All Solutions URL is canonical
    Given User inspects CTA URL
    When Checking URL format
    Then URL uses canonical /solutions/ path

  Scenario: Portfolio page unavailable handled
    Given /solutions/ page returns error
    When User clicks CTA
    Then Appropriate error handling occurs
