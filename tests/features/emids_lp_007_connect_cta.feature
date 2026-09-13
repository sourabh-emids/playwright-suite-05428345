Feature: Provide header Connect CTA

  Scenario: Verify Connect CTA is visually distinct
    Given The user views the header
    When The user identifies the Connect CTA among navigation items
    Then The Connect CTA is visually styled to stand out from standard navigation links

  Scenario: Verify Connect CTA has accessible name
    Given The user inspects the Connect CTA for accessibility
    When The CTA is read by screen reader or focused via keyboard
    Then The CTA has an accessible name that describes its action

  Scenario: Verify Connect routes to contact page
    Given The user clicks the Connect CTA
    When The CTA is activated via click or keyboard
    Then The CTA routes to the contact page URL '/contact/'

  Scenario: Verify CTA URL is HTTPS and valid
    Given The Connect CTA is rendered
    When The user inspects the CTA href attribute
    Then The URL uses HTTPS protocol and is a valid canonical destination

  Scenario: Verify CTA works with keyboard activation
    Given The user has keyboard focus on the Connect CTA
    When The user presses Enter or Space
    Then The CTA activates and navigates to the contact page

  Scenario: Verify no duplicate CTA in header
    Given The user views the complete header
    When The user counts Connect CTAs
    Then No duplicate Connect CTAs exist in the header
