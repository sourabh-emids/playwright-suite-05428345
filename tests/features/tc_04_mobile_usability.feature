Feature: Website remains usable in mobile view
  As a mobile visitor
  I want the homepage controls and content to remain usable
  So that I can access the website on a small screen

  Scenario: Core homepage content and mobile menu remain usable
    Given the homepage is opened in a mobile-sized browser
    When the visitor views the mobile homepage
    Then the mobile hero content and controls are visible
    When the visitor opens the mobile menu
    Then the mobile navigation control is usable
