Feature: Display CMS-0057 interoperability resource card

  Scenario: Verify CMS-0057 card renders with content
    Given CMS-0057 interoperability resource is configured
    When Insight card renders
    Then Card displays title, type, and action populated from approved content

  Scenario: Verify no empty title or destination
    Given CMS-0057 card is configured
    When Card renders
    Then Card has non-empty title and valid destination URL

  Scenario: Verify navigation to intended resource
    Given CMS-0057 card displays
    When User clicks the action
    Then Navigation leads to the intended CMS-0057 resource destination

  Scenario: Verify destination changed handled
    Given CMS-0057 resource destination has changed
    When User clicks action
    Then Card updates to current destination or appropriate redirect occurs
