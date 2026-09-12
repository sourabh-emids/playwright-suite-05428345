Feature: CMS-0057 interoperability resource card

  Scenario: CMS-0057 card renders with approved content
    Given CMS-0057 interoperability resource card
    When Content is verified
    Then Title, type, and action are populated from approved content

  Scenario: No empty title or destination
    Given CMS-0057 card
    When Required fields are checked
    Then Title and destination are populated

  Scenario: Card routes to intended resource
    Given CMS-0057 card action
    When Link is followed
    Then Navigates to configured resource destination
