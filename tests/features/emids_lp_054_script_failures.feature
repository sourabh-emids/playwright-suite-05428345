Feature: Handle script failures without breaking core content

  Scenario: Verify header remains readable when optional scripts fail
    Given Analytics, consent, media, or marketing scripts fail to load
    When Page renders
    Then Header navigation remains readable and functional

  Scenario: Verify main content remains readable when scripts fail
    Given Optional third-party scripts fail
    When Page renders
    Then Main content (hero, sections, CTAs) remains readable and complete

  Scenario: Verify CTAs remain navigable when scripts fail
    Given Third-party scripts are unavailable
    When Page renders
    Then All CTAs (header, hero, section, final) remain clickable and route correctly

  Scenario: Verify footer remains navigable when scripts fail
    Given Optional scripts fail
    When Page renders
    Then Footer remains fully readable with all links functional

  Scenario: Verify errors are contained
    Given Script failure occurs
    When Page renders
    Then Error is contained; does not cascade to break other functionality

  Scenario: Verify CSP block handled
    Given Content Security Policy blocks script
    When Page loads
    Then Core functionality preserved; blocked script fails gracefully

  Scenario: Verify DNS failure handled
    Given DNS resolution fails for third-party domain
    When Page loads
    Then Core page renders; failed integration handled gracefully

  Scenario: Verify ad blocker handled
    Given Ad blocker prevents script loading
    When Page renders
    Then Core content intact; blocked script does not break page

  Scenario: Verify timeout handled
    Given Third-party script loading times out
    When Page renders
    Then Core functionality continues; timeout handled without user-facing error

  Scenario: Verify malformed vendor script handled
    Given Third-party script contains errors
    When Script executes
    Then Error is caught; core page not broken; minimal logging captured
