@issue_0037
Feature: Google Tag Manager consent-governed loading

  As a user, I want Google Tag Manager to load only after consent
  so that my privacy is respected.

  Background:
    Given I navigate to the homepage

  Scenario: GTM does not load before consent
    When I have not given analytics consent
    Then GTM should not be active
