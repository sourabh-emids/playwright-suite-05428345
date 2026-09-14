Feature: Integrate ZoomInfo WebSights conditionally

  Scenario: Tooling loads conditionally based on enable state
    Given Visitor intelligence tooling is not enabled
    When Page renders
    Then ZoomInfo/WebSights does not load

  Scenario: Failure does not affect content or navigation
    Given Visitor intelligence tool fails
    When Page renders
    Then Content and navigation remain fully functional

  Scenario: Consent required for visitor intelligence
    Given Consent check for visitor intelligence
    When Tool attempts to load
    Then Tool loads only when permitted by consent

  Scenario: Private identifiers not in page copy
    Given Code review
    When Checking for hardcoded account IDs
    Then Private account identifiers are not exposed in visible page content

  Scenario: Vendor blocked handled
    Given Vendor domain blocked
    When Page renders
    Then Core functionality unaffected; blocked state logged

  Scenario: Network error handled
    Given Vendor request fails network error
    When Page renders
    Then Core page unaffected; error logged minimally

  Scenario: Integration logs sanitized
    Given Visitor intelligence integration error
    When Logging error
    Then Logs sanitized; no sensitive data captured
