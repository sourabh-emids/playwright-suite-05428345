Feature: All Solutions CTA functionality
  # issue_0016

  Scenario: All Solutions CTA is visible
    Given The Featured Solutions section is rendered
    When Visual inspection confirms CTA presence
    Then The All Solutions CTA is visible after or within the section

  Scenario: All Solutions CTA routes to portfolio
    Given A user clicks the All Solutions CTA
    When Navigation completes
    Then The user lands on /solutions/

  Scenario: All Solutions URL is canonical
    Given The CTA is rendered
    When Automated testing validates the URL
    Then The URL follows canonical format
