Feature: Global header visibility and Emids brand link

  Scenario: Header visible on initial page load
    Given User navigates to the Emids homepage
    When Page fully loads
    Then Global header is visible at the top of the viewport with Logo, Solutions, Capabilities, Industries, Insights, Company, and Connect fields

  Scenario: Emids logo returns to homepage
    Given User is on any page of the Emids website
    When User clicks the Emids logo or brand entry point
    Then User is navigated to the homepage URL '/'

  Scenario: All navigation items reachable by keyboard
    Given User navigates to the Emids homepage with keyboard focus at the header
    When User tabs through header navigation items
    Then Each navigation item (Solutions, Capabilities, Industries, Insights, Company) receives visible focus and can be activated with Enter key

  Scenario: All navigation items reachable by pointer
    Given User navigates to the Emids homepage
    When User hovers over each navigation item in the header
    Then Each navigation item is hoverable and clickable without dead links

  Scenario: Connect CTA routes to contact experience
    Given User is on the Emids homepage
    When User clicks the Connect CTA in the header
    Then User is navigated to the contact page at '/contact/'

  Scenario: No dead links in navigation
    Given User is on the Emids homepage
    When User clicks on each navigation item and CTA
    Then All navigation destinations resolve to valid internal or approved external URLs with HTTP 200 or appropriate redirect

  Scenario: Only one primary Connect CTA in header
    Given User is on the Emids homepage viewing the header
    When User inspects the header for Connect CTAs
    Then Exactly one primary Connect CTA is present in the header

  Scenario: Header accessible when JavaScript disabled
    Given User has JavaScript disabled in browser
    When User navigates to the Emids homepage
    Then Header is visible with functional navigation links

  Scenario: Header accessible at narrow viewport
    Given User views the Emids homepage at a narrow viewport width (320px)
    When Header renders
    Then All navigation destinations remain accessible via collapsible/responsive mechanism

  Scenario: Desktop header presents grouped navigation
    Given User views the Emids homepage on desktop
    When Header renders
    Then Navigation items are presented in grouped format as per design
