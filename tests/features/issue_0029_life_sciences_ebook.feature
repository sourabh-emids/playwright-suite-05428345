"""Feature file for Issue 0029 - Life Sciences transformation eBook card."""
Feature: Life Sciences transformation eBook card

  Scenario: Life Sciences eBook card renders correctly
    Given A user views the Life Sciences transformation eBook card
    When The card renders
    Then Card displays 'Unlocking Trusted Digital Transformation in Life Sciences' with eBook type and Download action

  Scenario: Life Sciences eBook routes to access page
    Given A user clicks the Download action on the Life Sciences eBook card
    When The action is activated
    Then User is navigated to /insights/unlocking-trusted-digital-transformation-in-life-sciences/

  Scenario: Canonical detail URL required
    Given A user examines the Life Sciences eBook card URL
    When The URL is analyzed
    Then The URL is canonical to the current detail page
