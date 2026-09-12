Feature: Life Sciences transformation eBook card

  Scenario: Life Sciences eBook renders correctly
    Given Life Sciences transformation eBook card
    When Card is verified
    Then Title shows 'Unlocking Trusted Digital Transformation in Life Sciences'

  Scenario: Correct canonical URL
    Given Life Sciences eBook card destination
    When URL is verified
    Then Card routes to /insights/unlocking-trusted-digital-transformation-in-life-sciences/

  Scenario: Download action opens correct experience
    Given Download CTA on card
    When Clicked
    Then Opens correct detail/access experience
