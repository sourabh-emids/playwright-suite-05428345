"""Feature file for Issue 0003 - Capabilities mega-menu functionality."""
Feature: Capabilities mega-menu functionality

  Scenario: Capabilities menu opens and closes predictably
    Given A user is viewing the Emids homepage desktop header
    When The user activates the Capabilities navigation item
    Then The menu opens displaying AI, Engineering, and Platforms capability groups

  Scenario: All capability links keyboard operable
    Given A user has the Capabilities menu open
    When The user tabs through the menu items
    Then All capability links are keyboard accessible and operable

  Scenario: Capability labels match site taxonomy
    Given A user has the Capabilities menu open
    When The user examines the group labels
    Then Labels match the approved site taxonomy and are unique within the menu

  Scenario: Capability URLs resolve correctly
    Given A user has the Capabilities menu open
    When The user clicks on any capability link
    Then The destination URL resolves to a valid page

  Scenario: Touch device capability menu access
    Given A user is on a touch device without hover capability
    When The user taps the Capabilities item
    Then The menu opens and all links are accessible via touch
