"""Feature file for Issue 0027 - Medicare Advantage eBook card display."""
Feature: Medicare Advantage eBook card display

  Scenario: Correct title, type, and Download action displayed
    Given A user views the Medicare Advantage eBook card
    When The card renders
    Then Card displays title 'Managing the Margin Reset in Medicare Advantage', eBook type, and Download action

  Scenario: Medicare Advantage eBook imagery if available
    Given The Medicare Advantage eBook has imagery configured
    When The card renders
    Then Image is displayed; card renders without broken image if image is unavailable

  Scenario: Medicare Advantage eBook URL resolves
    Given A user clicks the Medicare Advantage eBook card
    When The Download action is activated
    Then The user is navigated to /insights/managing-the-margin-reset-in-medicare-advantage/

  Scenario: Resource removed handling
    Given The Medicare Advantage resource is removed or gated differently
    When The card renders
    Then Appropriate handling occurs (redirect, unavailable message, or card excluded)
