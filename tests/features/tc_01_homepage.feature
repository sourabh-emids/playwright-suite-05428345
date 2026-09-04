@TC-01
Feature: Emids homepage availability
  As a public website visitor
  I want the Emids homepage to load successfully
  So that I can access its content without an obvious error

  Scenario: Website homepage opens successfully
    Given the user opens the Emids homepage
    Then the homepage loads successfully
    And no obvious error page is displayed
