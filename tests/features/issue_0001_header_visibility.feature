"""Feature file for Issue 0001 - Header visibility and Emids branding."""
Feature: Header visibility and Emids branding

  Scenario: Header visible on initial page load
    Given A user navigates to the Emids homepage
    When The page finishes loading
    Then The global header is visible and displays Emids branding

  Scenario: Emids logo returns to homepage
    Given A user is on any page of the Emids site
    When The user clicks the Emids logo or brand link
    Then The user is navigated to the homepage

  Scenario: Navigation items keyboard accessible
    Given A user is viewing the Emids homepage with keyboard-only navigation
    When The user tabs through the header navigation items
    Then All top-level navigation items are reachable and focusable

  Scenario: Connect CTA routes to contact experience
    Given A user is viewing the Emids homepage
    When The user clicks the Connect CTA in the header
    Then The user is navigated to the contact experience at /contact/

  Scenario: No dead links in header navigation
    Given A user is viewing the Emids homepage header
    When The user clicks on each navigation item
    Then All navigation destinations resolve to valid pages with no 404 errors

  Scenario: Single primary Connect CTA
    Given A user is viewing the Emids homepage header
    When The user examines the header for CTAs
    Then Only one primary Connect CTA is visible in the header
