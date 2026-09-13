Feature: Insights navigation group implementation

  Scenario: Insights control opens reliably
    Given User is on Emids homepage
    When User activates Insights navigation
    Then Insights menu opens reliably

  Scenario: Child links are readable at all breakpoints
    Given Insights menu is open
    When User views menu at desktop, tablet, and mobile widths
    Then Child links are readable and text does not overflow or become inaccessible

  Scenario: Child links operable at all breakpoints
    Given Insights menu is open
    When User tests navigation at different viewport sizes
    Then All child links remain operable via keyboard and pointer

  Scenario: No empty menu groups
    Given Insights menu is open
    When User views all menu groups
    Then No empty menu groups are displayed

  Scenario: Destination URLs are canonical
    Given Insights menu is open
    When User inspects child link URLs
    Then All destination URLs are canonical

  Scenario: Menu consistent with other navigation groups
    Given User is on Emids homepage
    When User views Insights menu
    Then Menu behavior is consistent with Solutions, Capabilities, and Industries mega-menu/disclosure patterns
