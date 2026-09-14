Feature: Render Insights section with six cards

  Scenario: Six cards render with content type title and image
    Given User views Insights section
    When Counting cards
    Then Six insight cards are visible, each with content type, title, and image where configured

  Scenario: Cards have appropriate action labels
    Given User examines card actions
    When Checking CTA labels
    Then Cards display appropriate action labels: Download for eBooks, Read More for articles

  Scenario: Cards accessible at all breakpoints
    Given User views Insights on mobile and desktop
    When Checking card accessibility
    Then All six cards remain accessible and operable at all supported breakpoints

  Scenario: Card titles and URLs required
    Given CMS content validation
    When Checking required fields
    Then Each card has non-empty title and valid URL

  Scenario: Action label matches content flow
    Given User reviews card CTA labels
    When Checking label accuracy
    Then Download used for downloadable resources; Read More for article navigation

  Scenario: Published content only rendered
    Given Some insight content is unpublished
    When Page renders
    Then Only published insights display; unpublished items excluded

  Scenario: Resource unpublished handled
    Given An insight card links to unpublished resource
    When Page renders
    Then Card either not rendered or shows appropriate unavailable state

  Scenario: Missing image handled gracefully
    Given Insight card has no image configured
    When Page renders
    Then Card renders with placeholder or without image; no broken image shown

  Scenario: Long title truncation handled
    Given Insight title is very long
    When Card renders at standard width
    Then Long title either displays fully or truncates with ellipsis; does not break layout

  Scenario: URL changes handled
    Given Insight resource URL has changed
    When User clicks card
    Then Navigation either resolves to new URL or broken link is detected in QA
