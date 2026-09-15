Feature: Main navigation menu items work correctly

  Scenario: Verify each main menu item opens correct page
    Given The homepage is loaded and main menu is visible
    When The user clicks on each main navigation menu item
    Then Each menu item navigates to the correct corresponding page
