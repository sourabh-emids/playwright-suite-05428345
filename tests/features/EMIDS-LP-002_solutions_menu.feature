Feature: Solutions mega-menu implementation

  Scenario: Solutions menu opens with accessible controls
    Given A user hovers over or focuses on the Solutions navigation item
    When The Solutions control is activated
    Then An accessible mega-menu opens displaying solution taxonomy grouped appropriately

  Scenario: All solution links are selectable
    Given The Solutions mega-menu is open
    When The user selects each visible solution link
    Then Each link navigates to its intended destination with non-empty label and valid URL

  Scenario: Keyboard focus within mega-menu
    Given The Solutions mega-menu is open
    When The user tabs through the menu items
    Then Focus remains within expected navigation order; tabbing through closes menu and returns focus to trigger

  Scenario: Solutions menu on touch device
    Given A user on a touch-only device
    When Tapping the Solutions menu trigger
    Then Menu opens with disclosure or drawer pattern; all solution links are reachable

  Scenario: Solutions menu not clipped by viewport
    Given The Solutions mega-menu is opened
    When The menu dimensions are checked against viewport
    Then Menu is not clipped and all content is visible
