Feature: Main navigation menu items functionality

  Scenario: All main menu items navigate to correct pages
    Given The user is on the homepage of the website
    When The user clicks on each main navigation menu item including but not limited to Home, About, Services, Solutions, Insights, Careers, and Contact
    Then Each menu item successfully navigates to its corresponding page and the correct page content is displayed matching the selected menu option

  Scenario: Menu hover states are visible
    Given The user is on the homepage
    When The user hovers over each main navigation menu item
    Then Visual hover indicators such as color changes, underlines, or highlighting are displayed to provide feedback on the interactive element

  Scenario: Menu items are clickable and responsive
    Given The user has loaded the homepage on a desktop browser
    When The user clicks on a navigation menu item multiple times in quick succession
    Then Each click is registered properly and navigation occurs without errors, double-clicks do not open duplicate tabs or cause page glitches

  Scenario: Dropdown submenus function correctly
    Given The user is on the homepage and there are menu items with dropdown submenus
    When The user hovers over or clicks on a parent menu item that has submenus
    Then The dropdown submenu appears with all submenu items visible and each submenu item navigates to the correct page when clicked
