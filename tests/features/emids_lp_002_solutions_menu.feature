Feature: Implement Solutions mega-menu

  Scenario: Verify Solutions menu opens and displays content
    Given The user hovers or focuses on the Solutions navigation item
    When The user activates the Solutions control
    Then An accessible mega-menu opens displaying solution group headings, solution labels, and URLs

  Scenario: Verify all solution links are selectable
    Given The Solutions mega-menu is open
    When The user tabs to or hovers over any solution link
    Then All visible solution links are keyboard selectable and pointer-clickable

  Scenario: Verify focus remains within navigation order
    Given The Solutions mega-menu is open and user focus is on a solution link
    When The user presses Tab to navigate forward
    Then Focus follows expected visual navigation order within the menu

  Scenario: Verify closing restores focus to trigger
    Given The Solutions mega-menu is open
    When The user closes the menu via Escape or clicking outside
    Then Focus returns to the Solutions trigger control

  Scenario: Verify mobile uses disclosure pattern
    Given The user is on a mobile device or narrow viewport
    When The user activates Solutions navigation
    Then An accessible disclosure or drawer pattern is used instead of mega-menu layout

  Scenario: Verify menu does not clip by viewport
    Given The user is on a tablet or narrow desktop viewport
    When The Solutions mega-menu opens
    Then Menu is positioned to remain fully visible within the viewport

  Scenario: Verify each item has valid URL
    Given The Solutions mega-menu is open
    When The user inspects each solution item
    Then Every item has a non-empty label and a valid internal or approved external URL
