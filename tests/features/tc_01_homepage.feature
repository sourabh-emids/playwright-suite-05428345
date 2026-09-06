@TC-01
Feature: Website homepage loads successfully
  The public homepage should be available without visible errors or broken
  critical content.

  Scenario: Open the Emids homepage
    Given the Emids homepage is opened
    Then the homepage is displayed without visible errors or broken critical content
