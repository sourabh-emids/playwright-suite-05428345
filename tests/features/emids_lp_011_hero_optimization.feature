Feature: Optimize hero media loading

  Scenario: Verify text remains available if media fails
    Given Hero media fails to load
    When The page renders
    Then Text content remains visible and accessible

  Scenario: Verify media dimensions reserved to avoid layout shift
    Given Hero media is configured with dimensions
    When The page loads before media downloads
    Then Space is reserved for media preventing layout shift (CLS)

  Scenario: Verify appropriately sized assets served
    Given Hero media is configured with srcset/sizes
    When The page loads at different viewport sizes
    Then Appropriately sized assets are served for the viewport

  Scenario: Verify principal LCP asset not lazy-loaded
    Given Hero contains principal LCP media asset
    When The page loads
    Then The principal LCP asset is not lazy-loaded to avoid harming LCP metric

  Scenario: Verify media loads progressively without moving text
    Given Hero media is loading
    When The page initially renders and media loads
    Then Text content position remains stable throughout loading

  Scenario: Verify CDN timeout handled gracefully
    Given CDN serving hero media is slow or times out
    When The page loads
    Then Text content renders while media gracefully fails or retries

  Scenario: Verify low-bandwidth connection handled
    Given User is on low-bandwidth connection
    When Hero media attempts to load
    Then Optimized or compressed media loads or gracefully degrades
