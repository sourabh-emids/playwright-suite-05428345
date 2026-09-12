Feature: Hero media loading optimization

  Scenario: Text content available if media fails
    Given Hero media fails to load
    When Page renders
    Then Text content remains visible and accessible

  Scenario: Media dimensions reserved to avoid layout shift
    Given Hero media container
    When Media dimensions are specified
    Then Layout space is reserved preventing CLS (Cumulative Layout Shift)

  Scenario: Appropriately sized assets served
    Given Hero media assets
    When Asset sizes are verified
    Then Assets are optimized for their display size

  Scenario: LCP asset not lazy-loaded
    Given Hero LCP (Largest Contentful Paint) element
    When Asset loading strategy is reviewed
    Then LCP asset is not lazy-loaded to prevent LCP degradation

  Scenario: Media loads progressively
    Given Hero section
    When Media loads
    Then Media loads progressively without moving primary text

  Scenario: Media on slow network
    Given Slow network conditions
    When Hero loads
    Then Text remains readable while media loads
