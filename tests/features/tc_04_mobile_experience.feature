@TC-04
Feature: Responsive mobile experience
  As a visitor using a mobile browser
  I want website content and controls to remain visible and usable
  So that I can use the website on a small screen

  Background:
    Given the Emids homepage is open at a 390 by 844 mobile viewport

  Scenario: Homepage content remains visible in mobile view
    Then the homepage text and logo are visible without horizontal overflow

  Scenario: Main menu is usable in mobile view
    When the user opens the mobile menu and the Solutions section
    Then the mobile Solutions menu is visible and usable

  Scenario: Primary button navigates in mobile view
    When the user selects the mobile homepage primary call to action
    Then the Forward Deployed Context Engineering page opens
