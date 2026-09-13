Feature: Engineering capability content render
  # issue_0022

  Scenario: Engineering label and content render correctly
    Given The Engineering capability card/panel is rendered
    When Visual inspection runs
    Then The Engineering label is displayed with supporting content

  Scenario: Engineering capability link is operable
    Given The Engineering capability card/panel is rendered
    When The Engineering CTA or link is clicked
    Then Navigation to the Engineering capability destination occurs

  Scenario: Engineering capability title is present
    Given The Engineering capability content is managed by CMS
    When Automated testing validates required fields
    Then Title field is non-empty
