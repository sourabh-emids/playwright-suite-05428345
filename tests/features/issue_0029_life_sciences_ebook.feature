Feature: Display Life Sciences eBook card

  Scenario: Life Sciences eBook card renders
    Given User views Insights section
    When Locating specific card
    Then Card titled 'Unlocking Trusted Digital Transformation in Life Sciences' displays

  Scenario: eBook Download action routes correctly
    Given User clicks Download on Life Sciences card
    When Navigation occurs
    Then User navigates to /insights/unlocking-trusted-digital-transformation-in-life-sciences/

  Scenario: Canonical detail URL validated
    Given User inspects URL
    When Checking URL format
    Then URL is canonical path to Life Sciences resource

  Scenario: Resource access flow unavailable handled
    Given Resource access flow is down
    When User clicks Download
    Then User sees appropriate error or fallback experience
