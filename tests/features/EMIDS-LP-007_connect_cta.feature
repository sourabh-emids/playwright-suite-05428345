Feature: Header Connect CTA implementation

  Scenario: Connect CTA is visually distinct
    Given The header is rendered
    When Visual inspection of the Connect CTA
    Then CTA has distinct styling that differentiates it from navigation links

  Scenario: Connect CTA has accessible name
    Given The Connect CTA element
    When Checked for accessibility
    Then CTA has descriptive accessible name identifying its purpose

  Scenario: Connect CTA routes to contact page
    Given The Connect CTA is clicked
    When Navigation is executed
    Then User reaches the contact page at /contact/

  Scenario: Connect CTA keyboard activation
    Given The Connect CTA has focus
    When User presses Enter or Space
    Then CTA activates and navigates to contact page

  Scenario: Connect CTA URL is HTTPS and valid
    Given The Connect CTA destination
    When URL is inspected
    Then URL uses HTTPS protocol and is valid
