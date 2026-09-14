Feature: Provide responsive layout across viewports

  Scenario: No horizontal scrolling at supported widths
    Given User views page at desktop, tablet, and mobile widths
    When Checking horizontal scroll
    Then No unintended horizontal scrolling occurs

  Scenario: Typography readable at all breakpoints
    Given User views text content at various sizes
    When Checking font sizes
    Then Text remains legible; font sizes appropriate for viewport

  Scenario: Controls do not overlap
    Given User views interactive elements
    When Checking layout at various widths
    Then Interactive elements do not overlap or become inaccessible

  Scenario: All cards sections remain available
    Given User views at mobile width
    When Checking content visibility
    Then All section content accessible via vertical scroll

  Scenario: Images preserve aspect ratio
    Given User views images across viewport sizes
    when Checking responsiveness
    Then Images scale proportionally; aspect ratio maintained

  Scenario: Content usable at 320px width
    Given User views page at minimum supported width
    When Checking layout
    Then Content fully usable; horizontal scroll not required

  Scenario: Content usable at 200% zoom
    Given User sets browser zoom to 200%
    When Viewing page
    Then Content usable without horizontal scroll

  Scenario: Very long text handled
    Given Content has unusually long text strings
    When Page renders at various widths
    Then Long text wraps or truncates gracefully without breaking layout

  Scenario: Browser zoom test at various levels
    Given User sets browser zoom between 100-200%
    When Checking layout stability
    Then Layout remains stable; content accessible

  Scenario: Landscape phone orientation
    Given User rotates phone to landscape
    When Page renders
    Then Content reflows appropriately for landscape orientation

  Scenario: Tablet split-screen supported
    Given User uses tablet in split-screen mode
    When Page renders in narrow width
    Then Content adapts to reduced width gracefully
