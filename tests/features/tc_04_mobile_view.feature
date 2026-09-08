@TC-04
Feature: Emids responsive mobile experience
  As a mobile website visitor
  I want content and controls to remain accessible
  So that I can use the website on a supported mobile viewport

  Scenario: Website remains visible and usable in mobile view
    Given the browser uses a 390 by 844 mobile viewport
    When the Emids homepage is opened in mobile view
    Then the mobile logo, primary text, image, and call-to-action are visible
    When the mobile navigation menu and Solutions section are opened
    Then the mobile navigation controls are visible and operable
    And the page has no horizontal content overflow
