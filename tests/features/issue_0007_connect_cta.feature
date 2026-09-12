"""Feature file for Issue 0007 - Header Connect CTA functionality."""
Feature: Header Connect CTA functionality

  Scenario: Connect CTA visually distinct
    Given A user is viewing the Emids homepage header
    When The user examines the Connect CTA
    Then The CTA is visually distinct from other navigation elements

  Scenario: Connect CTA has accessible name
    Given A user is viewing the Connect CTA
    When The user or assistive technology examines the CTA
    Then The CTA has an accessible name that describes its action

  Scenario: Connect CTA routes to contact page
    Given A user clicks the Connect CTA
    When The CTA is activated
    Then The user is navigated to /contact/ with valid HTTPS URL

  Scenario: Connect CTA keyboard activation
    Given A user is viewing the Emids homepage with keyboard navigation
    When The user focuses on and activates the Connect CTA
    Then The action is triggered successfully via keyboard

  Scenario: Contact page unavailable graceful handling
    Given The contact page is unavailable (503 or timeout)
    When A user clicks the Connect CTA
    Then An appropriate error message or fallback is displayed without breaking the UI
