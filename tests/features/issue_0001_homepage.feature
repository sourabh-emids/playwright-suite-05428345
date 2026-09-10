@issue_0001 @homepage
Feature: Website homepage loads successfully

  Scenario: Homepage renders without an obvious user-facing error
    Given the Emids website is available
    When the user opens the Emids homepage
    Then the homepage loads with its expected content and no obvious error page
