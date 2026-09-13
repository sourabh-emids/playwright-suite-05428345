Feature: Load Google Tag Manager container with consent governance

  Scenario: Verify core page works if GTM fails
    Given GTM container fails to load
    When Page renders
    Then Core page content and functionality remain intact

  Scenario: Verify non-essential tags wait for consent
    Given Non-essential tags are configured in GTM
    When Page loads with tags pending consent
    Then Non-essential tags do not fire before required consent is granted

  Scenario: Verify GTM does not block rendering
    Given GTM container script loads
    When Page renders
    Then Page rendering is not blocked by GTM script loading

  Scenario: Verify ad blocker handled
    Given Ad blocker prevents GTM loading
    When Page loads
    Then Core page remains functional; GTM failure is handled gracefully

  Scenario: Verify CSP block handled
    Given Content Security Policy blocks GTM
    When Page loads
    Then Core functionality remains; GTM failure logged minimally

  Scenario: Verify GTM timeout handled
    Given GTM script loading times out
    When Page renders
    Then Core page renders without waiting indefinitely for GTM

  Scenario: Verify consent denied handled
    Given User has not granted consent for GTM categories
    When Page loads
    Then GTM tags remain dormant; page functions normally
