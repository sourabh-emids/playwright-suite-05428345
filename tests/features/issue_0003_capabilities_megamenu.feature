Feature: Capabilities mega-menu implementation

  Scenario: Capabilities menu opens predictably
    Given User is on Emids homepage
    When User activates the Capabilities navigation item
    Then Menu opens with AI, Engineering, and Platforms capability groups visible

  Scenario: All capability links are keyboard operable
    Given Capabilities menu is open
    When User navigates with Tab key through capability links
    Then All capability links are keyboard accessible and operable

  Scenario: Labels match approved site taxonomy
    Given Capabilities menu is open
    When User views capability group labels
    Then Labels (AI, Engineering, Platforms) match approved site taxonomy with unique labels within menu

  Scenario: Desktop uses grouped mega-menu
    Given User is on desktop viewing Emids homepage
    When User activates Capabilities
    Then Desktop uses grouped mega-menu layout

  Scenario: Mobile uses accessible disclosure
    Given User is on mobile viewing Emids homepage
    When User activates Capabilities
    Then Mobile uses accessible disclosure pattern

  Scenario: No duplicate labels in capability menu
    Given Capabilities menu is open
    When User reviews all labels
    Then All capability labels are unique within the menu

  Scenario: All capability URLs resolve
    Given Capabilities menu is open
    When User clicks on each capability link
    Then All capability destination URLs resolve to valid pages
