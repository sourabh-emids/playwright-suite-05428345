Feature: Display Life Sciences transformation eBook card

  Scenario: Verify correct title for Life Sciences eBook
    Given Life Sciences transformation eBook is configured
    When Insight card renders
    Then Card displays title 'Unlocking Trusted Digital Transformation in Life Sciences'

  Scenario: Verify Download action works correctly
    Given Life Sciences eBook card renders
    When User clicks Download
    Then User is directed to correct detail/access experience

  Scenario: Verify canonical URL used
    Given Life Sciences eBook is configured
    When User inspects card URL
    Then URL resolves to canonical destination '/insights/unlocking-trusted-digital-transformation-in-life-sciences/'

  Scenario: Verify resource access flow unavailable handled
    Given Resource access flow is unavailable
    When User clicks Download
    Then Graceful error handling without page break
