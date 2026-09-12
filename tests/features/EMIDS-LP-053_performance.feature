Feature: Performance and Core Web Vitals optimization

  Scenario: Critical content renders without analytics wait
    Given Page load with analytics scripts
    When Page starts rendering
    Then Critical content renders without waiting for analytics

  Scenario: Images are sized and optimized
    Given Page images
    When Asset optimization is verified
    Then Images are appropriately sized and optimized

  Scenario: Below-fold media lazy-loaded appropriately
    Given Below-fold media assets
    When Loading strategy is verified
    Then Media is lazy-loaded where appropriate

  Scenario: Layout shifts minimized
    Given Page load performance
    When CLS is measured
    Then Layout shifts are minimized

  Scenario: Third-party scripts async/deferred
    Given Third-party script loading
    When Scripts are verified
    Then Scripts are loaded async/defer or consent-gated

  Scenario: No large unoptimized assets
    Given Page assets
    When Asset sizes are reviewed
    Then Large unoptimized assets are avoided

  Scenario: Slow network performance
    Given Throttled network conditions
    When Page loads
    Then Critical content remains accessible
