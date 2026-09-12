Feature: AI ROI eBook card display

  Scenario: AI ROI eBook renders with correct labeling
    Given AI ROI eBook card
    When Card is verified
    Then Title shows 'Closing the AI ROI Gap in Healthcare', type is eBook, expected action present

  Scenario: Published content and valid URL
    Given AI ROI eBook card
    When Content status and URL are verified
    Then Content is published and URL is valid
