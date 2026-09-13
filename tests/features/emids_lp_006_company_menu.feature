Feature: Implement Company navigation group

  Scenario: Verify Company menu exposes approved links
    Given The Company menu is open
    When The user inspects the menu content
    Then Only approved company links and Contact/Connect destinations are displayed

  Scenario: Verify keyboard, pointer, and touch interaction
    Given The Company menu is open
    When The user tests interaction via keyboard, mouse, and touch
    Then All menu items are operable using keyboard alone, pointer click, and touch tap

  Scenario: Verify unpublished pages do not appear
    Given A company page is unpublished in CMS
    When The Company menu renders
    Then Only published pages appear in the navigation

  Scenario: Verify no redirect loop occurs
    Given The Company menu contains linked pages
    When The user clicks a company navigation link
    Then Navigation completes without entering an infinite redirect loop

  Scenario: Verify focus not trapped in menu
    Given The Company menu is open and focus is inside
    When The user presses Tab multiple times
    Then Focus can exit the menu normally and does not become trapped
