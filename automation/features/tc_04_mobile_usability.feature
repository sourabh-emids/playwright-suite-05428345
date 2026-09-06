@tc_04
Feature: TC-04 Responsive mobile usability

  Scenario: Website content and controls remain usable in a mobile view
    Given the Emids homepage is open in a mobile-sized viewport
    When the user opens the mobile navigation menu
    Then the homepage text, logo, call to action, and mobile menu are usable
    When the user selects Connect from the mobile menu
    Then the contact page opens without horizontal page overflow
