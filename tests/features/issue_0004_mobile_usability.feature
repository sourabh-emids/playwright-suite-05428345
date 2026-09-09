@issue_0004
Feature: Mobile homepage usability

  Scenario: Content, navigation, and primary controls remain usable on mobile
    Given the homepage is open in the approved mobile viewport
    Then the mobile hero text, logo, and primary call to action are usable
    When the user opens the mobile menu and selects Contact Us
    Then the contact page opens in the mobile viewport
