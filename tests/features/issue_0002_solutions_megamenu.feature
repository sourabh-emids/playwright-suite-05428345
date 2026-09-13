Feature: Solutions mega-menu implementation

  Scenario: Solutions menu opens with keyboard
    Given User is on Emids homepage with keyboard focus on header
    When User tabs to Solutions and presses Enter or Space
    Then Solutions accessible menu opens and focus remains within expected navigation order

  Scenario: Solutions menu opens with pointer
    Given User hovers over Solutions navigation item
    When Hover interaction occurs
    Then Solutions accessible menu opens

  Scenario: Solutions menu opens with touch
    Given User is on touch device viewing Emids homepage
    When User taps on Solutions navigation item
    Then Solutions menu opens (equivalent disclosure/drawer pattern on mobile)

  Scenario: All solution links are selectable
    Given Solutions menu is open
    When User views solution items
    Then All visible solution links are selectable and have non-empty labels with valid URLs

  Scenario: Solutions menu closes and restores focus
    Given Solutions menu is open with focus on trigger
    When User presses Escape or clicks outside
    Then Menu closes and focus returns to the trigger element

  Scenario: Solutions menu not clipped by viewport
    Given Solutions menu is open
    When Menu contains many items
    Then Menu does not clip or overflow viewport boundaries

  Scenario: Mobile uses disclosure pattern
    Given User is on mobile device viewing Emids homepage
    When User taps Solutions
    Then Mobile uses disclosure/drawer pattern equivalent to desktop mega-menu
