@TC-03
Feature: Primary call-to-action destinations
  As a website visitor
  I want prominent calls to action to open their intended content
  So that I can continue the relevant journey

  Scenario: Contact Us opens the contact page
    Given the Emids homepage is open in a desktop browser
    When the user selects Contact Us from the Company menu
    Then the Emids contact page opens

  Scenario: Homepage primary call to action opens its expected page
    Given the Emids homepage is open in a desktop browser
    When the user selects the homepage primary call to action
    Then the Forward Deployed Context Engineering page opens
