@TC-04 @non-functional @responsive
Feature: Website remains usable in mobile view
  Text, branding, navigation, and calls to action must remain visible and usable.

  Scenario: Use the homepage at a 390 by 844 mobile viewport
    Given the browser uses a 390 by 844 mobile viewport
    When the user opens the Emids homepage
    Then the main mobile text, image, menu control, and call-to-action are visible
    When the user opens the mobile menu
    Then the mobile navigation is visible and usable
