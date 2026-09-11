Feature: TC-04 Mobile website usability
  Verify essential content, navigation, and calls to action remain usable at a mobile viewport size.

  Scenario: Homepage content and mobile navigation are usable
    Given the TC-04 user opens the homepage in a mobile-sized browser window
    Then the TC-04 essential homepage content and controls are usable
    When the TC-04 user opens the mobile navigation menu
    Then the TC-04 mobile navigation and its primary button are usable
