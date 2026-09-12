Feature: AI capability content rendering

  Scenario: AI label and supporting content render
    Given AI capability card/panel
    When Content is verified
    Then AI label and supporting content are present

  Scenario: AI relevant link is operable
    Given AI capability CTA/link
    When Link is tested
    Then Link navigates to valid AI capability destination

  Scenario: AI title required
    Given AI capability content
    When Title field is checked
    Then Title is populated

  Scenario: Missing AI destination handling
    Given Edge case where AI destination is broken
    When Link is clicked
    Then Appropriate error handling occurs
