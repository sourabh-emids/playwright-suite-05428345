Feature: Payer data readiness blog card

  Scenario: Payer data readiness blog displays correctly
    Given Payer data readiness blog card
    When Card is verified
    Then Title shows 'Payers: Is Your Data Ready for AI?', type is Blog, Read More action shown

  Scenario: Read More action for blog content
    Given Blog card CTA
    When Label is verified
    Then CTA label reads 'Read More' (reflecting article navigation, not file download)

  Scenario: Correct blog destination
    Given Blog card link
    When URL is verified
    Then Link opens correct article/detail experience
