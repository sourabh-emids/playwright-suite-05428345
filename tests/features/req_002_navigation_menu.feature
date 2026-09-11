@REQ-002
Feature: Main navigation menu items navigate to correct pages

  @functional @navigation
  Scenario: Navigation menu items open correct destination pages
    Given User is on the homepage with main navigation menu visible
    When User clicks on each main navigation menu item
    Then Each menu item opens the correct associated page or section as expected
    And The destination page loads with relevant content matching the menu label

  @functional @navigation
  Scenario: Solutions navigation opens Solutions page
    Given User is on the homepage
    When User clicks on "Solutions" in the main navigation
    Then The Solutions page should load with the URL containing "solutions"

  @functional @navigation
  Scenario: Capabilities navigation opens Capabilities page
    Given User is on the homepage
    When User clicks on "Capabilities" in the main navigation
    Then The Capabilities page should load with the URL containing "capabilities"

  @functional @navigation
  Scenario: Industries navigation opens Industries page
    Given User is on the homepage
    When User clicks on "Industries" in the main navigation
    Then The Industries page should load with the URL containing "segments"

  @functional @navigation
  Scenario: Insights navigation opens Insights page
    Given User is on the homepage
    When User clicks on "Insights" in the main navigation
    Then The Insights page should load with the URL containing "insights"

  @functional @navigation
  Scenario: Company navigation opens About Us page
    Given User is on the homepage
    When User clicks on "Company" in the main navigation
    Then The About Us page should load with the URL containing "about-us"

  @functional @navigation
  Scenario: Connect navigation opens Contact page
    Given User is on the homepage
    When User clicks on "Connect" in the main navigation
    Then The Contact page should load with the URL containing "contact"
