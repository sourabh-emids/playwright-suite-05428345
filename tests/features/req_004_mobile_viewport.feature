@REQ-004
Feature: Website displays correctly on mobile viewport

  @functional @responsive_design
  Scenario: Mobile layout renders all core content without horizontal scrolling
    Given User accesses the website using a mobile-sized browser window or device
    When The homepage loads in mobile viewport
    Then Text, images, menu and buttons are visible and usable without horizontal scrolling for core content

  @functional @responsive_design
  Scenario: Mobile navigation menu is accessible
    Given User accesses the website using a mobile-sized browser window or device
    When The homepage loads in mobile viewport
    Then A mobile menu toggle button should be visible

  @functional @responsive_design
  Scenario: Mobile viewport shows all key page elements
    Given User accesses the website using a mobile-sized browser window or device
    When The homepage loads in mobile viewport
    Then The main heading should be visible
    And The logo should be visible
    And The page title should be correct
