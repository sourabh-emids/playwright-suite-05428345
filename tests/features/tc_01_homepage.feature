@TC-01
Feature: Emids homepage availability
  As a public website visitor
  I want the homepage to load successfully
  So that I can access its primary content

  Scenario: Website homepage opens successfully
    Given the public Emids homepage is opened
    Then the primary homepage content is visible
    And no visible page load failure is shown
