Feature: Insights section and six content cards

  Scenario: Six insight cards render
    Given User views Insights section
    When Page renders
    Then Six insight/resource cards are rendered

  Scenario: Cards contain content type
    Given Insight cards render
    When User views each card
    Then Each card displays content type (eBook, Blog, etc.)

  Scenario: Cards contain title
    Given Insight cards render
    When User views each card
    Then Each card displays a title

  Scenario: Cards contain image where configured
    Given Insight cards render
    When User views each card
    Then Image is displayed where configured

  Scenario: Cards contain Download or Read More action
    Given Insight cards render
    When User views each card
    Then Each card displays Download or Read More action with appropriate label

  Scenario: Cards accessible at all breakpoints
    Given User views Insights section at mobile, tablet, and desktop widths
    When Page renders
    Then Cards remain accessible and content visible

  Scenario: Published content only
    Given Insight cards render
    When User validates content
    Then Only published content is displayed

  Scenario: Title and URL required
    Given Insight cards render
    When User validates each card
    Then Each card has non-empty title and valid URL

  Scenario: Action label matches content flow
    Given Insight cards render
    When User views action labels
    Then Action labels match content flow (Download for eBooks, Read More for articles)

  Scenario: Resource unpublished handling
    Given One resource is unpublished
    When Page renders
    Then Card either shows updated content or appropriate placeholder

  Scenario: Missing image handling
    Given Card image is missing
    When Page renders
    Then Placeholder or fallback displays appropriately

  Scenario: Long title handling
    Given Card has very long title
    When Page renders at narrow viewport
    Then Title wraps appropriately without breaking layout
