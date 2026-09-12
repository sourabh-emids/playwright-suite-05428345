"""Feature file for Issue 0013 - See the model CTA functionality."""
Feature: See the model CTA functionality

  Scenario: See the model CTA routes to FDCE detail
    Given A user is viewing the How We Deliver section
    When The user clicks the See the model CTA
    Then The user is navigated to /forward-deployed-context-engineering/

  Scenario: See the model CTA keyboard operable
    Given A user is navigating with keyboard
    When The user focuses on and activates the See the model CTA
    Then The action is triggered successfully

  Scenario: See the model CTA has accessible name
    Given A user or assistive technology examines the CTA
    When The CTA is present
    Then The accessible name describes the action ('See the model' or similar)

  Scenario: FDCE destination 404 handling
    Given The FDCE detail page returns 404
    When A user clicks the See the model CTA
    Then An appropriate error page is displayed
