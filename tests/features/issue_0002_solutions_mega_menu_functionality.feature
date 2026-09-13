Feature: Solutions mega-menu functionality
  # issue_0002

  Scenario: Solutions menu opens with accessible controls
    Given A user is viewing the desktop header
    When The user clicks or focuses on the Solutions navigation item
    Then An accessible menu opens displaying solution groups with headings and solution labels

  Scenario: All solution links are selectable
    Given The Solutions menu is open
    When The user clicks on any solution link
    Then The link navigates to a valid destination URL

  Scenario: Keyboard navigation maintains expected order
    Given The Solutions menu is open and user focuses on the trigger
    When The user navigates using keyboard within the menu
    Then Focus moves through solution links in a logical order matching visual layout

  Scenario: Closing menu restores focus to trigger
    Given The Solutions menu is open and user has focus within it
    When The user closes the menu via Escape key or click outside
    Then Focus returns to the Solutions navigation trigger

  Scenario: Mobile Solutions uses disclosure pattern
    Given A user is viewing the site on a mobile device
    When The user taps the Solutions navigation item
    Then A mobile-appropriate disclosure or drawer pattern opens with equivalent content

  Scenario: Solution items have valid URLs
    Given The Solutions menu is rendered
    When Automated testing validates each item
    Then Every solution item has a non-empty label and a valid internal or approved external URL
