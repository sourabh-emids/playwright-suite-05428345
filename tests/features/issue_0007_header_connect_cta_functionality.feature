Feature: Header Connect CTA functionality
  # issue_0007

  Scenario: Connect CTA is visually distinct
    Given A user views the global header
    When The user visually scans the header
    Then The Connect CTA is visually distinct from other navigation items

  Scenario: Connect CTA has accessible name
    Given A user or assistive technology accesses the Connect CTA
    When Screen reader or accessibility tool reads the element
    Then The CTA has an accessible name that describes its action

  Scenario: Connect CTA routes to contact page
    Given A user clicks the Connect CTA
    When The navigation action completes
    Then The user lands on the contact page at /contact/

  Scenario: Connect CTA is keyboard operable
    Given A user navigates using keyboard only
    When Focus reaches the Connect CTA and user presses Enter
    Then Navigation to the contact page occurs

  Scenario: Connect CTA URL is valid HTTPS
    Given The Connect CTA is rendered
    When Automated testing validates the URL
    Then The URL is valid and uses the HTTPS protocol
