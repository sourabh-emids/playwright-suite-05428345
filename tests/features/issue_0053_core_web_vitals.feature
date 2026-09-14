Feature: Meet Core Web Vitals performance goals

  Scenario: Critical content renders without waiting for analytics
    Given Page load with analytics scripts
    When Measuring LCP
    Then LCP element renders before analytics scripts block rendering

  Scenario: Images optimized and sized appropriately
    Given User views images across viewport sizes
    When Checking image requests
    Then Appropriately sized images served for viewport; no unnecessarily large images

  Scenario: Below-fold media lazy-loaded appropriately
    Given User scrolls page
    When Monitoring network requests
    Then Below-fold images and media lazy-load as they approach viewport

  Scenario: Layout shifts minimized
    Given User loads page
    When Measuring CLS
    Then Cumulative Layout Shift score meets target thresholds

  Scenario: Third-party scripts async deferred or consent-gated
    Given Third-party script tags
    When Checking script loading strategy
    Then Scripts use async, defer, or are gated by consent

  Scenario: No large unoptimized assets
    Given Asset audit
    When Checking file sizes
    Then Assets optimized; large unoptimized files flagged

  Scenario: Visually unchanged with progressive enhancement
    Given User compares optimized vs baseline page
    When Visual comparison
    Then Visual appearance identical; performance improved

  Scenario: Slow network media loading
    Given User on slow connection
    When Page loads
    Then Critical content loads first; media loads progressively

  Scenario: Blocked third parties handled
    Given Third-party domains blocked
    When Page renders
    Then Core content loads; blocked scripts handled gracefully

  Scenario: Cached stale asset detection
    Given Cached asset version mismatch
    When Page renders
    Then Cache busting mechanism ensures fresh assets load

  Scenario: Large viewport image optimization
    Given User on large high-DPI display
    When Checking image serving
    Then Appropriate resolution images served; not unnecessarily oversized

  Scenario: Web Vitals telemetry with consent
    Given User has granted performance analytics consent
    When Measuring performance
    Then Web Vitals data collected; no sensitive dimensions captured
