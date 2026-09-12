Feature: ZoomInfo/WebSights conditional integration

  Scenario: Tooling loads conditionally
    Given ZoomInfo/WebSights configuration
    When Enabled and permitted by consent
    Then Tooling loads

  Scenario: Failure does not affect content or navigation
    Given ZoomInfo/WebSights fails to load
    When Page renders
    Then Content and navigation remain functional

  Scenario: No private identifiers in page copy
    Given ZoomInfo/WebSights integration
    When Page content is reviewed
    Then Private account identifiers are not exposed in page copy
