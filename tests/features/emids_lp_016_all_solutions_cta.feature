Feature: Provide All Solutions CTA

  Scenario: Verify All Solutions CTA is visible
    Given The Featured Solutions section renders
    When The user views the section
    Then All Solutions CTA is visible within or after the section

  Scenario: Verify CTA routes to solutions portfolio
    Given The All Solutions CTA is rendered
    When User clicks the CTA
    Then The CTA routes to '/solutions/'

  Scenario: Verify CTA URL is canonical
    Given The All Solutions CTA renders
    When The user inspects the href
    Then URL is canonical HTTPS destination

  Scenario: Verify portfolio page unavailable handled
    Given Solutions portfolio page is unavailable
    When User clicks All Solutions CTA
    Then Appropriate error or fallback displayed
