Feature: Integrate ZoomInfo/WebSights conditionally

  Scenario: Verify tooling loads conditionally
    Given ZoomInfo/WebSights is configured and enabled
    When Page loads with appropriate consent
    Then Tooling loads when enabled and permitted

  Scenario: Verify failure does not affect content
    Given ZoomInfo/WebSights fails to load
    When Page renders
    Then Page content and navigation remain unaffected

  Scenario: Verify consent category required
    Given ZoomInfo/WebSights is configured
    When User denies required consent category
    Then Tooling does not load

  Scenario: Verify private identifiers not exposed in page copy
    Given ZoomInfo/WebSights configuration exists
    When User views page content
    Then Private account identifiers are not exposed in visible page copy

  Scenario: Verify vendor blocked handled
    Given Vendor domain is blocked
    When Page loads
    Then Core functionality remains; integration fails gracefully

  Scenario: Verify network error handled
    Given Network error prevents ZoomInfo/WebSights loading
    When Page renders
    Then Core page renders normally; error logged minimally

  Scenario: Verify consent revoked handled
    Given User previously allowed visitor intelligence
    When User revokes consent
    Then Tooling stops; page remains functional
