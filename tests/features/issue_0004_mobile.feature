@issue_0004 @mobile
Feature: Website remains usable in a mobile-sized viewport

  Scenario: Core homepage content and controls remain usable on mobile
    Given the Emids homepage is open in a 390 by 844 mobile viewport
    Then the core text, brand image, menu control, and primary action are visible
    When the user opens the mobile menu
    Then the mobile navigation and contact action are visible and usable
    When the user closes the menu and selects the primary homepage action
    Then the primary action destination opens in the mobile viewport
