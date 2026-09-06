@TC-04
Feature: Website remains usable in mobile view
  Text, images, menu controls, and actions should remain visible and usable at
  the agreed mobile viewport.

  Scenario: View and navigate the homepage at mobile size
    Given the Emids homepage is open at the agreed mobile viewport
    Then the primary mobile content and controls are visible and usable
    When the user navigates to Solutions with the mobile menu
    Then the Solutions page is displayed in mobile view
