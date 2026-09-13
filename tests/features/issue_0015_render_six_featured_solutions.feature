Feature: Render six featured solutions
  # issue_0015

  Scenario: All six solution entries are present
    Given The Featured Solutions section is rendered
    When Automated testing counts solution items
    Then Exactly six featured solution items are displayed

  Scenario: Numbering 01-06 is correct
    Given The Featured Solutions section is rendered
    When Visual inspection confirms numbering
    Then Items are numbered 01, 02, 03, 04, 05, 06 in the correct order

  Scenario: Each entry has readable title and summary
    Given Any featured solution item
    When Content is analyzed
    Then The item contains a non-blank title and supporting summary text

  Scenario: Each entry has intended destination
    Given The Featured Solutions items are rendered
    When URLs are validated
    Then Each solution item links to a valid destination URL

  Scenario: Solution titles include Modernization as a Service
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Modernization as a Service' as the title

  Scenario: Solution titles include Interoperability
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Interoperability' as the title

  Scenario: Solution titles include Cloud Migration
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Cloud Migration' as the title

  Scenario: Solution titles include Global Capability Center
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Global Capability Center' as the title

  Scenario: Solution titles include Epic Implementation
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Epic Implementation' as the title

  Scenario: Solution titles include Agentic AI
    Given The Featured Solutions section loads
    When Content is verified
    Then One item contains 'Agentic AI' as the title
