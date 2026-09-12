@issue_0014
Feature: Semantic heading hierarchy and landmarks

  As a user, I want the page to have proper semantic structure
  so that screen readers and assistive technologies work correctly.

  Background:
    Given I navigate to the homepage

  Scenario: Page has proper heading hierarchy
    When I view the page
    Then the heading hierarchy should follow logical order
    And there should be a single H1
    And H2 headings should be used for section titles
    And H3 headings should be used for subsection titles

  Scenario: Page has proper landmark regions
    When I view the page
    Then there should be a header landmark
    And there should be a main landmark
    And there should be a footer landmark
