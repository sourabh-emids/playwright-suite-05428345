Feature: Engineering capability content rendering

  Scenario: Engineering label and supporting content render
    Given Engineering capability card/panel
    When Content is verified
    Then Engineering label and supporting content are present

  Scenario: Engineering relevant link is operable
    Given Engineering capability CTA/link
    When Link is tested
    Then Link navigates to valid engineering capability destination

  Scenario: Engineering title required
    Given Engineering capability content
    When Title field is checked
    Then Title is populated
