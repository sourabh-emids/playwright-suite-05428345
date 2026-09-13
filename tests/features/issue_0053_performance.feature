Feature: Performance and Core Web Vitals goals

  Scenario: Critical content renders without analytics
    Given Analytics scripts are loading or blocked
    When Page loads
    Then Critical content renders without waiting for analytics

  Scenario: Images optimized and sized
    Given Images render on page
    When Assets are loaded
    Then Images are optimized and appropriately sized for viewport

  Scenario: Below-fold media lazy-loaded
    Given Below-fold media exists
    When Page loads
    Then Below-fold media is lazy-loaded where appropriate

  Scenario: Layout shifts minimized
    Given User views page
    When Page loads
    Then Layout shifts are minimized

  Scenario: Third-party scripts deferred
    Given Third-party scripts are configured
    When Page loads
    Then Scripts use async/defer or are consent-gated

  Scenario: No large unoptimized assets
    Given Assets are configured
    When Page loads
    Then Large unoptimized assets are avoided

  Scenario: Slow network handling
    Given User is on slow network
    When Page loads
    Then Critical content remains accessible

  Scenario: Blocked third parties handling
    Given Third parties are blocked
    When Page loads
    Then Critical content loads appropriately

  Scenario: Cached stale asset handling
    Given Stale asset is cached
    When Page loads
    Then Fresh content is served appropriately

  Scenario: Large viewport image handling
    Given User views page on large desktop
    When Images load
    Then Appropriately sized images are served
