Feature: Meet performance and Core Web Vitals goals

  Scenario: Verify critical content renders without waiting for analytics
    Given Analytics scripts are loading
    When Page loads initial content
    Then Critical content renders immediately without waiting for analytics to complete

  Scenario: Verify images are sized and optimized
    Given Page contains images
    When Images render
    Then Images are appropriately sized for viewport; formats are optimized (WebP, AVIF where supported)

  Scenario: Verify below-fold media lazy-loaded appropriately
    Given Page has below-fold media content
    When Page loads initial viewport
    Then Below-fold media is lazy-loaded to improve initial load performance

  Scenario: Verify layout shifts minimized
    Given Page renders with media and dynamic content
    When Page loads and media finishes loading
    Then Cumulative Layout Shift (CLS) is minimized; space is reserved for media

  Scenario: Verify third-party scripts use async/defer/consent-gating
    Given Third-party scripts (analytics, marketing, media) are configured
    When Page loads
    Then Scripts use async/defer attributes or are gated by consent as appropriate

  Scenario: Verify slow network handled
    Given User is on slow network connection
    When Page loads
    Then Critical content remains accessible; lazy-loaded content loads progressively

  Scenario: Verify blocked third parties handled
    Given Third-party scripts are blocked by extension or settings
    When Page loads
    Then Core functionality remains intact; no blocking errors displayed to user

  Scenario: Verify cached stale asset handled
    Given Browser serves cached version of asset
    When Page renders with stale asset
    Then Critical content renders; caching strategy minimizes staleness issues

  Scenario: Verify large viewport image optimized
    Given User is on large viewport (e.g., 4K monitor)
    When Page loads
    Then Appropriately sized image is served; not unnecessarily downscaled from smaller version
