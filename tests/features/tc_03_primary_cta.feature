@TC-03
Feature: Primary calls to action open expected destinations
  Important contact and information calls to action should take users to the
  content they identify.

  Scenario: Contact Us opens the contact page
    Given a page with the Contact Us call to action is open
    When the user selects Contact Us
    Then the contact page is displayed

  Scenario: Learn More opens the identified partner page
    Given the partnerships page with Learn More calls to action is open
    When the user selects Learn More for Snowflake
    Then the Snowflake partner page is displayed
