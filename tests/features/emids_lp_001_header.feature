Feature: Render global header and Emids brand entry point

  Scenario: Verify header renders on initial page load
    Given The user navigates to the homepage
    When The page finishes loading
    Then The global header is visible with all navigation fields displayed

  Scenario: Verify Emids logo navigates to homepage
    Given The user is on any page of the website
    When The user clicks the Emids logo or brand link in the header
    Then The user is navigated to the homepage URL '/'

  Scenario: Verify all navigation items reachable via keyboard
    Given The user has keyboard focus on the header
    When The user tabs through navigation items including Logo, Solutions, Capabilities, Industries, Insights, Company, and Connect
    Then Each item receives visible focus and is activatable with Enter or Space key

  Scenario: Verify Connect CTA routes to contact page
    Given The user views the header
    When The user clicks the Connect CTA
    Then The user is navigated to the contact experience URL '/contact/'

  Scenario: Verify single primary Connect CTA
    Given The user views the header navigation
    When The user counts all Connect CTAs in the header
    Then Only one primary Connect CTA is present in the header region

  Scenario: Verify no dead links in navigation
    Given The user is on the homepage
    When The user navigates to each navigation item destination via keyboard
    Then All navigation links resolve to valid destinations with no 404 errors

  Scenario: Verify navigation at narrow viewport
    Given The user is viewing the site at mobile width (320px)
    When The page loads or is resized
    Then Navigation collapses responsively without losing access to any destination

  Scenario: Verify page functionality when JS is disabled
    Given The user has JavaScript disabled in browser
    When The user loads the homepage
    Then Header navigation remains accessible and functional via standard links
