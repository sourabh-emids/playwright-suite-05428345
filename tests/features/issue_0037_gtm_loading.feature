Feature: Google Tag Manager container loading

  Scenario: Core page works if GTM fails
    Given Google Tag Manager fails to load
    When Page renders
    Then Core page content and functionality remain intact

  Scenario: Non-essential tags gated by consent
    Given Non-essential tags are configured in GTM
    When Required consent has not been given
    Then Non-essential tags do not run before required consent

  Scenario: GTM does not block rendering
    Given GTM script loads
    When Page renders
    Then GTM loading is non-blocking and does not prevent page rendering

  Scenario: Ad blocker handling
    Given Ad blocker is active
    When GTM attempts to load
    Then Core page remains functional

  Scenario: CSP block handling
    Given Content Security Policy blocks GTM
    When Page loads
    Then Core functionality remains intact

  Scenario: GTM timeout handling
    Given GTM script times out
    When Page loads
    Then Core page continues to function

  Scenario: Consent denied handling
    Given User has denied analytics consent
    When GTM loads
    Then GTM respects consent configuration
