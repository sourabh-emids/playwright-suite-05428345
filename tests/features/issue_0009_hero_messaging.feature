"""Feature file for Issue 0009 - Hero messaging and visual rendering."""
Feature: Hero messaging and visual rendering

  Scenario: Primary H1 is present on hero
    Given A user loads the Emids homepage
    When The page loads completely
    Then Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'

  Scenario: Supporting content readable
    Given A user views the hero section
    When The user examines the supporting copy
    Then Supporting content is readable and not truncated

  Scenario: Hero media has alternative handling
    Given A user is viewing the hero with assistive technology
    When The screen reader encounters the hero media
    Then Appropriate alternative text or aria-label is provided

  Scenario: Hero CTA visible without deep scrolling
    Given A user loads the Emids homepage on a common desktop viewport
    When The page loads and the user has not scrolled
    Then The hero CTA is visible above or before deep page scrolling

  Scenario: H1 is non-empty and unique
    Given A user or search engine examines the page
    When The page HTML is analyzed
    Then The H1 is non-empty and unique (no other H1 elements on the page)

  Scenario: Hero media URL resolves
    Given A user views the hero section
    When The page loads the hero media
    Then The media URL resolves successfully

  Scenario: Hero rendering at small viewport
    Given A user is viewing the site on a mobile device (320px width)
    When The page loads
    Then Hero content renders properly without horizontal scrolling

  Scenario: Hero with reduced motion preference
    Given A user has prefers-reduced-motion enabled
    When The page loads
    Then Hero animations are reduced or eliminated
