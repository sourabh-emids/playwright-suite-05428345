@REQ-001
Feature: Homepage loads successfully

  @smoke
  Scenario: Homepage loads without errors
    Given User navigates to the website URL "https://www.emids.com/"
    When The browser initiates and completes the page load request
    Then Homepage loads successfully without obvious errors, broken layouts, or missing critical content

  @smoke
  Scenario: Homepage renders all visible elements correctly
    Given User has successfully loaded the homepage
    When Page resources finish rendering (images, scripts, stylesheets)
    Then All visible elements display correctly and the page becomes interactive
    And The page title should be "Emids - Digital Engineering, Core Platforms, and AI Solutions"
    And The main heading should be visible
