Feature: All Solutions CTA implementation

  Scenario: All Solutions CTA visible and routes correctly
    Given The All Solutions CTA in Featured Solutions section
    When Inspected for visibility and destination
    Then CTA is visible after/within the section and routes to /solutions/

  Scenario: CTA URL is canonical
    given All Solutions CTA destination
    When URL is verified
    Then URL uses canonical format

  Scenario: Portfolio page unavailable fallback
    Given Edge case where solutions portfolio is unavailable
    When CTA is clicked
    Then Appropriate error handling or redirect occurs
