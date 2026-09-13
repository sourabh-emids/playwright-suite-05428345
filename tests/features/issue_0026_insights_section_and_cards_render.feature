Feature: Insights section and cards render
  # issue_0026

  Scenario: Six insight cards render
    Given The Insights section is rendered
    When Automated testing counts cards
    Then Exactly six insight cards are displayed

  Scenario: Cards contain required content fields
    Given Each insight card is analyzed
    When Required fields are validated
    Then Each card contains: content type, title, image (where configured), and Download or Read More action

  Scenario: Cards accessible at all breakpoints
    Given The Insights section is rendered
    When Viewport is tested at desktop, tablet, and mobile widths
    Then Cards remain accessible and functional at all breakpoints

  Scenario: Only published content displayed
    Given Insight cards are rendered
    When Automated testing validates content status
    Then Only published content is displayed

  Scenario: Card titles and URLs are required
    Given Insight cards are managed by CMS
    When Required field validation runs
    Then Each card has a non-empty title and valid URL
