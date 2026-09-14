Feature: Implement Solutions mega-menu

  Scenario: Solutions menu opens and displays solution groups
    Given User is on desktop with header visible
    When User clicks or activates the Solutions navigation item
    Then Accessible mega-menu opens displaying solution group headings and solution labels

  Scenario: All solution links are selectable
    Given Solutions mega-menu is open
    When User clicks on any visible solution link
    Then User is navigated to the solution destination URL

  Scenario: Solutions menu keyboard navigation maintains focus order
    Given User navigates Solutions menu using keyboard
    When User tabs through menu items
    Then Focus remains within the menu and follows logical visual order

  Scenario: Closing solutions menu restores focus to trigger
    Given Solutions mega-menu is open
    When User closes the menu via Escape key or click outside
    Then Focus returns to the Solutions trigger control

  Scenario: Mobile solutions disclosure pattern
    Given User is on mobile device viewing header
    When User expands Solutions section
    Then Equivalent disclosure or drawer pattern displays solution items

  Scenario: Solution items have valid labels and URLs
    Given Solutions menu is open
    When User inspects solution items
    Then Each item has non-empty label and valid internal or approved external URL

  Scenario: Mega-menu not clipped by viewport
    Given User has narrow browser window
    When Solutions menu opens
    Then Menu is not clipped by viewport edges and remains fully visible
