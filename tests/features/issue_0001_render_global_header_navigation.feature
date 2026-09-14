"""Feature: Render Global Header Navigation."""
Feature: Render Global Header Navigation

  @issue_0001
  Scenario: header_visible_on_initial_load
    Given User navigates to the homepage
    When Page loads completely
    Then Header is visible with logo, navigation items, and Connect CTA

  @issue_0001
  Scenario: logo_returns_to_homepage
    Given User is on any page within the site
    When User clicks the Emids logo
    Then User is returned to the homepage

  @issue_0001
  Scenario: keyboard_navigation_all_items
    Given User focuses on the header using keyboard only
    When User tabs through navigation items
    Then All top-level navigation items are reachable and focusable

  @issue_0001
  Scenario: pointer_navigation_all_items
    Given User hovers over the header
    When User moves pointer over each navigation item
    Then All top-level navigation items are clickable and respond to hover

  @issue_0001
  Scenario: connect_routes_to_contact
    Given User is on any page
    When User clicks the Connect CTA in the header
    Then User is routed to the contact experience page

  @issue_0001
  Scenario: single_primary_connect_cta
    Given Header is rendered
    When Count of primary Connect CTAs is checked
    Then Only one primary Connect CTA is present in the header

  @issue_0001
  Scenario: missing_logo_asset_handling
    Given Logo asset is missing or fails to load
    When Page renders
    Then Header remains functional and alternative text or brand name is displayed

  @issue_0001
  Scenario: long_menu_label_handling
    Given Navigation item has a long label
    When Header renders at maximum viewport width
    Then Long labels are handled gracefully without breaking layout

  @issue_0001
  Scenario: js_disabled_header_accessibility
    Given JavaScript is disabled in browser
    When User interacts with header
    Then Header navigation remains accessible via links

  @issue_0001
  Scenario: narrow_viewport_navigation_access
    Given Page is viewed at narrow viewport (mobile)
    When Navigation collapses
    Then All navigation destinations remain accessible via menu trigger
