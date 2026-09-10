@issue_0003 @cta
Feature: Primary call-to-action buttons open expected destinations

  Scenario: Contact and learn-more calls to action open their intended pages
    Given the Emids homepage containing primary calls to action is open
    When the user selects the Contact Us action labelled "Connect"
    Then the contact page opens
    When the user returns home and selects the learn-more action labelled "See How We Deliver Outcomes"
    Then the forward-deployed context engineering page opens
