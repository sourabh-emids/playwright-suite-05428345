Feature: Render global header with Emids branding

  Scenario: Header visibility on initial page load
    Given User navigates to the emids.com homepage
    When Page finishes loading
    Then Global header is visible at the top of the viewport

  Scenario: Emids logo navigates to homepage
    Given User is on any page within the site
    When User clicks on the Emids logo or brand entry point
    Then User is navigated to the homepage URL '/'

  Scenario: All navigation items keyboard accessible
    Given User focuses on the header navigation area
    When User presses Tab key to cycle through navigation items
    Then All top-level navigation items receive visible focus and are reachable

  Scenario: Connect CTA routes to contact experience
    Given User is viewing the header on desktop or mobile
    When User clicks the Connect CTA
    Then User is navigated to the contact page at /contact/

  Scenario: Header displays all required navigation fields
    Given User views the desktop header
    When Navigation is fully expanded
    Then Logo, Solutions, Capabilities, Industries, Insights, Company, and Connect fields are all visible

  Scenario: Navigation has no dead links
    Given User hovers over any navigation item
    When All navigation items are tested for valid destinations
    Then Each navigation item has a configured non-empty URL and no dead links exist

  Scenario: Only one primary Connect CTA in header
    Given User views the header
    When User counts primary Connect CTA elements
    Then Exactly one prominent Connect CTA exists in the header

  Scenario: Responsive navigation preserves access on mobile
    Given User views the site on a narrow viewport mobile device
    When Navigation collapses into mobile menu
    Then All navigation destinations remain accessible through the mobile navigation interface

  Scenario: Long menu labels display correctly
    Given Navigation configuration contains a long menu label
    When Header renders with extended label text
    Then Long label displays without breaking layout or overlapping adjacent elements

  Scenario: Header renders when JavaScript is disabled
    Given User has JavaScript disabled in browser
    When User navigates to the homepage
    Then Header with navigation links is visible and functional
