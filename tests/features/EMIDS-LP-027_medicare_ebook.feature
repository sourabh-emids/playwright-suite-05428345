Feature: Medicare Advantage eBook card display

  Scenario: Medicare Advantage eBook renders correctly
    Given Medicare Advantage eBook card
    When Card is verified
    Then Title shows 'Managing the Margin Reset in Medicare Advantage', type is eBook, imagery displays if available, Download action present

  Scenario: Correct destination URL
    Given Medicare Advantage eBook card link
    When URL is inspected
    Then Card routes to current detail page at /insights/managing-the-margin-reset-in-medicare-advantage/
