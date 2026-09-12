Feature: Insights section and six content cards

  Scenario: Six cards render with complete content
    Given Insights section
    When Cards are counted
    Then Six cards render with content type, title, image (where configured), and Download or Read More action

  Scenario: Cards accessible at all breakpoints
    Given Insights cards at desktop, tablet, mobile widths
    When Responsive layout is tested
    Then All cards remain accessible and functional

  Scenario: Published content only
    Given Insight card content
    When Publication status is verified
    Then Only published content is displayed

  Scenario: Title and URL required
    Given Insight card data
    When Required fields are checked
    Then Title and URL are present for each card

  Scenario: Resource unpublished handling
    Given Edge case where resource is unpublished
    When Section renders
    Then Card is either hidden or shows appropriate state

  Scenario: Long title truncation
    Given Card with very long title
    When Content renders
    Then Title is handled appropriately without breaking layout
