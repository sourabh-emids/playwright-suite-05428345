Feature: Google Tag Manager with consent governance

  Scenario: Core page works if GTM fails
    Given GTM script fails to load or blocked
    When Page renders
    Then Core page functionality remains unaffected

  Scenario: Non-essential tags respect consent
    Given GTM container with consent-gated tags
    When Consent has not been granted
    Then Non-essential tags do not run before required consent

  Scenario: GTM does not block rendering
    Given GTM loading behavior
    When Page loads
    Then GTM script loads asynchronously without blocking page render

  Scenario: Consent signals properly configured
    Given GTM container configuration
    When Consent model is implemented
    Then Consent signals are properly integrated with GTM
