"""Feature file for Issue 0002 - Solutions mega-menu functionality."""
Feature: Solutions mega-menu functionality

  Scenario: Solutions menu opens and is accessible
    Given A user is viewing the Emids homepage desktop header
    When The user hovers or clicks on the Solutions navigation item
    Then An accessible mega-menu opens displaying the Solutions taxonomy

  Scenario: Solutions menu keyboard navigation
    Given A user is navigating the header with keyboard
    When The user focuses on Solutions and activates it
    Then The menu opens and all solution links are keyboard operable

  Scenario: Solutions menu closes and restores focus
    Given A user has the Solutions mega-menu open
    When The user closes the menu via keyboard or click outside
    Then Focus is restored to the Solutions trigger element

  Scenario: All solution links have valid URLs
    Given A user has the Solutions mega-menu open
    When The user examines the visible solution links
    Then Each solution item has a non-empty label and valid URL

  Scenario: Mobile solutions menu uses disclosure pattern
    Given A user is viewing the site on a mobile device
    When The user taps the Solutions navigation item
    Then An accessible disclosure or drawer pattern is displayed

  Scenario: Solutions menu viewport clipping prevention
    Given A user has the Solutions mega-menu open near the viewport edge
    When The mega-menu is rendered
    Then The menu is not clipped by the viewport and remains fully visible
