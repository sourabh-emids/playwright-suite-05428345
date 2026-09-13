Feature: Hero media loading optimization
  # issue_0011

  Scenario: Text content available when media fails
    Given Hero media fails to load
    When The page renders
    Then Text content remains available and readable

  Scenario: Media dimensions reserved to avoid layout shift
    Given Hero media is configured with known dimensions
    When The page renders before media loads
    Then Placeholder space is reserved preventing cumulative layout shift

  Scenario: Appropriately sized assets served
    Given Hero media is requested
    When Automated testing validates asset sizes
    Then Optimized format and size are served based on viewport

  Scenario: Hero media not lazy-loaded harmfully
    Given The hero section contains the LCP element
    When Performance testing analyzes loading strategy
    Then The principal LCP image is not lazy-loaded to maintain LCP performance
