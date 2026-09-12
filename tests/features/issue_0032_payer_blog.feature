"""Feature file for Issue 0032 - Payer data readiness blog card."""
Feature: Payer data readiness blog card

  Scenario: Blog type and Read More action shown
    Given A user views the Payer data readiness blog card
    When The card renders
    Then Card shows type=Blog and CTA='Read More'

  Scenario: Blog routes to correct article experience
    Given A user clicks the Read More action on the blog card
    When The action is activated
    Then User is navigated to the correct article/detail experience

  Scenario: CTA reflects article navigation not file download
    Given A user examines the blog card CTA label
    When The label is analyzed
    Then CTA label reflects article navigation ('Read More') rather than file download ('Download')

  Scenario: Article moved handling
    Given The Payer data readiness article has been moved
    When A user clicks the Read More action
    Then Appropriate redirect or error handling occurs
