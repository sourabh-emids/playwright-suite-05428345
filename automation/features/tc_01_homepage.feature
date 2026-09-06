@tc_01
Feature: TC-01 Homepage availability

  Scenario: Homepage loads successfully
    Given the user has a supported browser and an active internet connection
    When the user opens the Emids homepage
    Then the homepage is displayed without a visible error or broken layout
