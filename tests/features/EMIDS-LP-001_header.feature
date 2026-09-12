Feature: Global header and Emids brand entry point

  Scenario: Header visibility on initial page load
    Given A user navigates to the homepage for the first time
    When The page loads completely
    Then The global header is visible at the top of the viewport with Emids logo, all navigation items (Solutions, Capabilities, Industries, Insights, Company), and Connect CTA

  Scenario: Emids logo navigates to homepage
    Given A user is on any page of the site
    When The user clicks the Emids logo or brand element
    Then The user is navigated to the homepage

  Scenario: Keyboard navigation to all top-level items
    Given A user navigates using keyboard only (Tab key)
    When The user tabs through the header navigation
    Then All top-level navigation items (Solutions, Capabilities, Industries, Insights, Company) are reachable and receive visible focus state; Connect CTA is reachable

  Scenario: Pointer navigation to all top-level items
    Given A user with a mouse or touch device
    When The user hovers over or taps each top-level navigation item
    Then All navigation items are interactive and show appropriate hover/focus states

  Scenario: Connect CTA routes to contact experience
    Given A user clicks the Connect CTA in the header
    When The Connect button or link is activated
    Then The user is navigated to the contact page

  Scenario: All navigation destinations are valid
    Given All navigation items in the header
    When Each navigation item is inspected for its destination URL
    Then All destinations are configured with valid URLs and no dead links exist

  Scenario: Single primary Connect CTA in header
    Given The header navigation items
    When Counting primary Connect CTA elements
    Then Only one primary Connect CTA is present in the header

  Scenario: Header accessibility with JS disabled
    Given JavaScript is disabled in the browser
    When The homepage loads
    Then Header is visible and basic navigation links are functional

  Scenario: Header on narrow viewport
    Given A user views the site on a mobile device with narrow viewport
    When The page renders at narrow width
    Then Navigation collapses appropriately but all destinations remain accessible
