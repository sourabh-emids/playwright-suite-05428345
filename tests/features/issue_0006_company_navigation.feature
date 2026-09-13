Feature: Company navigation group implementation

  Scenario: Company menu exposes approved company links
    Given Company menu is open
    When User views menu content
    Then Only published company pages are exposed

  Scenario: Company menu works with keyboard
    Given User is on Emids homepage with keyboard focus on header
    When User navigates to Company and opens menu
    Then Company menu items are keyboard accessible

  Scenario: Company menu works with pointer
    Given User is on Emids homepage
    When User hovers over Company navigation
    Then Company menu opens and items are clickable

  Scenario: Company menu works with touch
    Given User is on touch device viewing Emids homepage
    When User taps Company navigation
    Then Company menu opens via touch interaction

  Scenario: Contact destinations accessible via Company menu
    Given Company menu is open
    When User views Contact/Connect destinations
    Then Contact/Connect destinations are visible and accessible

  Scenario: No focus trap in Company menu
    Given Company menu is open with focus inside
    When User presses Tab to navigate through menu items
    Then Focus does not become trapped and exits menu appropriately

  Scenario: No redirect loops from Company links
    Given Company menu is open
    When User clicks on a company link
    Then Page does not enter a redirect loop
