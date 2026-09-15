Feature: Mobile responsive layout is usable

  Scenario: Verify mobile viewport displays all elements correctly
    Given A user has access to a web browser with mobile viewport
    When The website is opened in a mobile-sized browser window (e.g., 375x667)
    Then Text, images, menu, and buttons are visible and usable on the mobile view
