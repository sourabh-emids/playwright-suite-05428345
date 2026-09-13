Feature: Route hero CTA to FDCE experience

  Scenario: Verify hero CTA resolves to FDCE page
    Given The hero CTA is rendered
    When The user clicks or activates the hero CTA
    Then The CTA resolves to the canonical FDCE URL '/forward-deployed-context-engineering/'

  Scenario: Verify browser navigation behavior preserved
    Given The user clicks the hero CTA
    When The navigation occurs
    Then Standard browser navigation behavior is preserved (back button works, history updated)

  Scenario: Verify CTA URL is HTTPS and canonical
    Given The hero CTA is rendered
    When The user inspects the CTA href
    Then The URL uses HTTPS protocol and is canonical

  Scenario: Verify CTA works as link or button per design
    Given The hero CTA is rendered
    When The user activates the CTA via keyboard or click
    Then CTA behaves as a standard link or button per design specification

  Scenario: Verify new tab navigation works correctly
    Given The user right-clicks the hero CTA and selects 'Open in new tab'
    When The CTA opens in new tab
    Then FDCE destination loads correctly in new tab
