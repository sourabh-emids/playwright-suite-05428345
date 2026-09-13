Feature: Cookie Preferences control in footer
  # issue_0036

  Scenario: Cookie Preferences control visible in footer
    Given The footer is rendered
    When Visual inspection runs
    Then Cookie Preferences link/button is visible in the footer

  Scenario: Cookie Preferences opens consent UI
    Given A user clicks the Cookie Preferences control
    When Activation completes
    Then The consent management UI opens allowing user to revise or withdraw consent

  Scenario: Cookie Preferences available after initial banner dismissal
    Given The user has dismissed an initial cookie banner
    When The page continues to be used
    Then Cookie Preferences control remains available in the footer

---
Feature: Footer legal navigation render
  # issue_0045

  Scenario: Legal links have descriptive text and valid destinations
    Given The footer legal navigation is rendered
    When Links are analyzed
    Then Each link has descriptive text (Privacy Policy, Cookie Policy, Accessibility Statement, etc.) and resolves to a valid HTTPS URL

  Scenario: Legal links have visible focus states
    Given Keyboard navigation is tested
    When Focus reaches legal links
    Then Visible focus states are present

  Scenario: All legal URLs are HTTPS and published
    Given Legal navigation links are rendered
    When URL validation runs
    Then All URLs use HTTPS protocol and point to published pages

  Scenario: Legal link labels are not blank
    Given Legal navigation links are rendered
    When Automated testing validates label content
    Then No labels are blank

---
Feature: Footer corporate contact information
  # issue_0046

  Scenario: Footer information readable at mobile widths
    Given The footer is rendered at mobile viewport
    When Visual inspection runs
    Then Footer corporate information remains readable

  Scenario: Corporate info does not conflict with legal navigation
    Given The footer is rendered
    When Visual inspection runs
    Then Corporate/contact information layout does not overlap or conflict with legal navigation links

  Scenario: Social links resolve to valid destinations
    Given Social links are rendered in footer
    When URL validation runs
    Then Social link URLs resolve successfully

  Scenario: Only approved current content published
    Given Footer content is managed
    When Content is reviewed
    Then Only approved, current information is published
