Feature: AI capability content render
  # issue_0021

  Scenario: AI label and content render correctly
    Given The AI capability card/panel is rendered
    When Visual inspection runs
    Then The AI label is displayed with supporting content

  Scenario: AI capability link is operable
    Given The AI capability card/panel is rendered
    When The AI CTA or link is clicked
    Then Navigation to the AI capability destination occurs

  Scenario: AI capability title is present
    Given The AI capability content is managed by CMS
    When Automated testing validates required fields
    Then Title field is non-empty

  Scenario: AI capability URL is valid
    Given The AI capability link is rendered
    When Automated testing validates the URL
    Then The destination URL is valid and returns HTTP 200
