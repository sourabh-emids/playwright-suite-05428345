Feature: All Solutions CTA functionality

  Scenario: CTA visible within section
    Given User views Featured Solutions section
    When User looks for All Solutions CTA
    Then CTA is visible after or within the section

  Scenario: CTA routes to solutions portfolio
    Given User clicks All Solutions CTA
    When Navigation occurs
    Then User is navigated to '/solutions/'

  Scenario: URL is canonical
    Given User inspects All Solutions CTA URL
    When User examines href
    Then URL is canonical

  Scenario: Portfolio page unavailable handling
    Given User clicks All Solutions CTA
    When Portfolio page is unavailable
    Then User sees appropriate error or fallback
