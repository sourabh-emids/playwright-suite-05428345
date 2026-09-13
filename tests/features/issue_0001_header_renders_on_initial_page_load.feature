Feature: Render global header with navigation
  # issue_0001

  Scenario: Header renders on initial page load
    Given A user navigates to the emids.com homepage
    When The page has fully loaded
    Then The global header is visible and displays Emids logo, navigation items (Solutions, Capabilities, Industries, Insights, Company), and the Connect CTA

  Scenario: Emids logo returns to homepage
    Given A user is on any page within the site
    When The user clicks the Emids logo or brand link
    Then The user is navigated to the homepage at the root URL '/'

  Scenario: All navigation items keyboard accessible
    Given A user focuses on the header navigation
    When The user navigates using Tab key
    Then All top-level navigation items (Solutions, Capabilities, Industries, Insights, Company, Connect) are reachable by keyboard and have visible focus states

  Scenario: All navigation items pointer accessible
    Given A user is viewing the page with a pointer device
    When The user hovers over any navigation item
    Then All navigation items are clickable and show appropriate hover states

  Scenario: Connect CTA routes to contact experience
    Given A user is on the homepage
    When The user clicks the Connect CTA in the header
    Then The user is navigated to the contact page at the appropriate URL

  Scenario: Navigation has no dead links
    Given All navigation items are rendered in the header
    When Automated testing checks each navigation link
    Then All links resolve to valid destinations with HTTP 200 status

  Scenario: Only one primary Connect CTA exists
    Given The page has loaded with the global header
    When Automated testing counts Connect CTA elements
    Then Only one primary Connect CTA is present in the header
