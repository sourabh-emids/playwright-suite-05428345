"""Feature file for Issue 0016 - All Solutions CTA functionality."""
Feature: All Solutions CTA functionality

  Scenario: All Solutions CTA visible and routes correctly
    Given A user views the Featured Solutions section
    When The user clicks the All Solutions CTA
    Then The CTA routes to the solutions portfolio at /solutions/

  Scenario: All Solutions CTA canonical URL
    Given A user examines the All Solutions CTA URL
    When The URL is inspected
    Then The URL is canonical (/solutions/)

  Scenario: Portfolio page unavailable handling
    Given The solutions portfolio page is unavailable
    When A user clicks the All Solutions CTA
    Then An appropriate error handling occurs
