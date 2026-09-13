Feature: Render Insights section and six content cards

  Scenario: Verify six cards render
    Given Insights section renders
    When User counts content cards
    Then Exactly six insight/resource cards are displayed

  Scenario: Verify each card has type, title, and action
    Given Insight cards render
    When User inspects each card
    Then Each card displays content type, title, image where configured, and Download/Read More action

  Scenario: Verify cards accessible at all breakpoints
    Given Insights section renders
    When User views at mobile, tablet, and desktop
    Then All cards remain accessible and usable across breakpoints

  Scenario: Verify title and URL required
    Given Insight card is configured
    When Section renders
    Then Each card has non-empty title and valid destination URL

  Scenario: Verify action label matches content flow
    Given Insight cards render with different content types
    When User views action labels
    Then eBook-type cards show 'Download'; blog-type cards show 'Read More'

  Scenario: Verify published content only displayed
    Given Some insights are unpublished
    When Section renders
    Then Only published content appears in the section

  Scenario: Verify missing image handled
    Given An insight card has no image configured
    When Card renders
    Then Card renders with text content; no broken image placeholder

  Scenario: Verify very long title handled
    Given An insight card has very long title
    When Card renders
    Then Title wraps or truncates gracefully without breaking layout

  Scenario: Verify responsive card grid/rail
    Given Insight cards render
    When User views at different viewports
    Then Cards use responsive grid/rail layout with consistent heights where practical
