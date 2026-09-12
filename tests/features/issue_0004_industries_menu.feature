"""Feature file for Issue 0004 - Industries mega-menu functionality."""
Feature: Industries mega-menu functionality

  Scenario: Industries menu contains all five audiences
    Given A user has the Industries mega-menu open
    When The user examines the menu content
    Then All five audience destinations are present

  Scenario: Audience links keyboard accessible
    Given A user has the Industries menu open
    When The user navigates via keyboard
    Then Each of the five audience links is reachable without a mouse

  Scenario: Audience links use canonical URLs
    Given A user has the Industries menu open
    When The user examines the audience link URLs
    Then Links use canonical URLs

  Scenario: Mobile industries menu stacked display
    Given A user is viewing the site on a mobile device
    When The user taps the Industries navigation item
    Then A stacked list or disclosure pattern displays all five audiences

  Scenario: One segment unavailable graceful handling
    Given The Payer segment page is unpublished
    When A user views the Industries menu
    Then The menu either excludes the unpublished segment or displays it as inactive
