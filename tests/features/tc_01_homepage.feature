@TC-01 @functional @availability
Feature: Website homepage opens successfully
  The Emids homepage must load successfully without obvious browser errors.

  Scenario: Open the public homepage
    When the user opens the Emids homepage
    Then the homepage loads successfully without obvious errors
