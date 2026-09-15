Feature: Primary CTA buttons function properly

  Scenario: Verify Contact Us button works
    Given The homepage is loaded
    When The user clicks the Contact Us button
    Then The Contact Us page or form opens as expected

  Scenario: Verify Learn More button works
    Given The homepage is loaded
    When The user clicks a Learn More button
    Then The expected page or section opens correctly
