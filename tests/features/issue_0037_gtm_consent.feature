Feature: Load GTM with consent governance

  Scenario: Core page works if GTM fails
    Given Google Tag Manager fails to load
    When Page renders
    Then Core page content, navigation, and CTAs remain fully functional

  Scenario: Non-essential tags do not run before consent
    Given User has not given consent
    When GTM container loads
    Then Non-essential analytics/marketing tags do not fire

  Scenario: GTM does not block rendering
    Given User measures page load time
    When Checking GTM script loading
    Then GTM loads asynchronously; does not block first paint

  Scenario: GTM async or deferred loading
    Given Developer tools network tab
    When Checking GTM script tag
    Then GTM script has async or defer attribute

  Scenario: Ad blocker blocking GTM handled
    Given User has ad blocker enabled
    When Page renders
    Then Core functionality unaffected; GTM blocked gracefully

  Scenario: CSP block handled
    Given Content Security Policy blocks GTM
    When Page renders
    Then Core content loads; GTM failure logged minimally

  Scenario: GTM timeout handled
    Given GTM script takes too long to load
    When Timeout threshold reached
    Then Page continues without GTM; failure logged

  Scenario: Consent denied handled
    Given User denies analytics consent
    When GTM attempts to fire tags
    Then Tags respect consent state and do not fire
