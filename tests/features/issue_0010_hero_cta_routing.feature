"""Feature file for Issue 0010 - Hero CTA routing to FDCE experience."""
Feature: Hero CTA routing to FDCE experience

  Scenario: Hero CTA resolves to FDCE canonical page
    Given A user clicks the hero CTA
    When The CTA is activated
    Then The user is navigated to the canonical FDCE page at /forward-deployed-context-engineering/

  Scenario: Hero CTA uses HTTPS URL
    Given A user examines the hero CTA URL
    When The URL is inspected
    Then The URL is HTTPS and canonical

  Scenario: Hero CTA new tab behavior
    Given A user right-clicks or uses keyboard to open hero CTA in new tab
    When The action is performed
    Then The FDCE page opens in a new tab with expected behavior

  Scenario: FDCE destination unavailable handling
    Given The FDCE destination page is temporarily unavailable
    When A user clicks the hero CTA
    Then An appropriate error or redirect handling occurs
