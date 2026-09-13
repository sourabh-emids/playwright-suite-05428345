Feature: Hero CTA routes to FDCE
  # issue_0010

  Scenario: Hero CTA resolves to FDCE page
    Given The hero section is rendered with a CTA
    When A user clicks the hero CTA
    Then Navigation reaches the Forward-Deployed Context Engineering page at /forward-deployed-context-engineering/

  Scenario: Hero CTA URL uses HTTPS canonical
    Given The hero CTA is rendered
    When Automated testing validates the URL
    Then The URL is HTTPS and canonical

  Scenario: Hero CTA behaves as proper link or button
    Given The hero CTA is rendered
    When Accessibility testing analyzes the element
    Then The CTA functions as a semantic link or button with proper interactive behavior
