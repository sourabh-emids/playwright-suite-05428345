"""Feature: Header Connect CTA Functionality."""
Feature: Header Connect CTA Functionality

  @issue_0007
  Scenario: connect_cta_visually_distinct
    Given Header renders
    When Visual inspection of Connect CTA
    Then Connect CTA is visually distinct from other navigation elements

  @issue_0007
  Scenario: connect_cta_accessible_name
    Given Connect CTA is rendered
    When Screen reader or accessibility tool inspects the element
    Then CTA has accessible name that describes the action

  @issue_0007
  Scenario: connect_cta_routes_to_contact
    Given User clicks Connect CTA
    When Navigation completes
    Then User is on the contact page at /contact/

  @issue_0007
  Scenario: connect_cta_keyboard_activation
    Given Connect CTA is focused via keyboard
    When User activates (Enter/Space)
    Then CTA works with keyboard activation

  @issue_0007
  Scenario: connect_cta_https_url
    Given Connect CTA destination is configured
    When URL is validated
    Then CTA URL is valid and uses HTTPS

  @issue_0007
  Scenario: contact_page_unavailable_handling
    Given Contact page is unavailable or returns error
    When User clicks Connect CTA
    Then User sees appropriate error page or fallback

  @issue_0007
  Scenario: connect_cta_text_wrapping
    Given Header at narrow viewport
    When Connect CTA label is long
    Then Text wrapping does not break layout or accessibility
