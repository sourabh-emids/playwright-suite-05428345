Feature: Homepage loads successfully
  As a visitor
  I want the Emids homepage to be available
  So that I can use the website without obvious errors

  Scenario: The homepage opens without obvious errors
    Given the homepage is available
    When the visitor opens the Emids homepage
    Then the homepage is loaded and usable
    And no obvious error is displayed
