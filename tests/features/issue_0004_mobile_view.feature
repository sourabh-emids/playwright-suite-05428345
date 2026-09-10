Feature: Responsive mobile website experience

  Scenario: Website remains usable in a mobile-sized view
    Given the Emids homepage is open at the supported mobile viewport
    Then the homepage text, logo, primary action, and menu are visible
    When the user opens the mobile Solutions menu
    Then the Modernization navigation destination is accessible
    When the user selects the mobile Modernization destination
    Then the Modernization page opens in the mobile-sized view
