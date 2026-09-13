Feature: Medicare Advantage eBook card display
  # issue_0027

  Scenario: Medicare Advantage eBook card renders correctly
    Given The Insights section includes the Medicare Advantage resource
    When The card is rendered
    Then Title displays 'Managing the Margin Reset in Medicare Advantage' with eBook type and Download action

  Scenario: Medicare Advantage card image renders if available
    Given The Medicare Advantage eBook card is rendered
    When Image availability is checked
    Then The card displays imagery if available

  Scenario: Medicare Advantage Download routes to current detail page
    Given A user clicks the Download action on the Medicare Advantage card
    When Navigation completes
    Then The user reaches the resource detail/access page at the configured URL

---
Feature: CMS-0057 interoperability card display
  # issue_0028

  Scenario: CMS-0057 card renders with populated content
    Given The Insights section includes the CMS-0057 interoperability resource
    When The card is rendered
    Then Card title, type, and action are populated from approved content

  Scenario: CMS-0057 card navigates to intended resource
    Given A user clicks the CMS-0057 card action
    When Navigation completes
    Then The user reaches the configured resource destination

  Scenario: CMS-0057 card has no empty fields
    Given The CMS-0057 card is rendered
    When Automated testing validates required fields
    Then No empty title or destination fields exist

---
Feature: Life Sciences eBook card display
  # issue_0029

  Scenario: Life Sciences eBook card renders correctly
    Given The Insights section includes the Life Sciences transformation resource
    When The card is rendered
    Then Title displays 'Unlocking Trusted Digital Transformation in Life Sciences' with appropriate action

  Scenario: Life Sciences Download opens correct access experience
    Given A user clicks the Download action on the Life Sciences card
    When Navigation completes
    Then The user reaches the correct detail/access experience

  Scenario: Life Sciences card uses canonical detail URL
    Given The Life Sciences card action is configured
    When URL validation runs
    Then The URL follows canonical format at /insights/unlocking-trusted-digital-transformation-in-life-sciences/

---
Feature: AI ROI eBook card display
  # issue_0030

  Scenario: AI ROI eBook card renders correctly
    Given The Insights section includes the AI ROI resource
    When The card is rendered
    Then Title displays 'Closing the AI ROI Gap in Healthcare' with eBook labeling and expected action

  Scenario: AI ROI card has published content and valid URL
    Given The AI ROI eBook card is rendered
    When Validation testing runs
    Then Content is published and URL is valid

---
Feature: FinOps payer resource card display
  # issue_0031

  Scenario: FinOps payer resource card renders correctly
    Given The Insights section includes the FinOps healthcare payer resource
    When The card is rendered
    Then Card displays title, type, and action with correct routing

  Scenario: FinOps card has valid destination
    Given The FinOps card is rendered
    When URL validation runs
    Then The destination URL is valid

---
Feature: Payer data readiness blog card display
  # issue_0032

  Scenario: Payer data readiness blog card renders correctly
    Given The Insights section includes the payer data readiness blog
    When The card is rendered
    Then Title displays 'Payers: Is Your Data Ready for AI?' with type=Blog and Read More action

  Scenario: Blog Read More action opens correct article
    Given A user clicks the Read More action on the blog card
    When Navigation completes
    Then The user reaches the correct article/detail experience

  Scenario: Blog card CTA reflects article navigation
    Given The blog card CTA is rendered
    When Label is verified
    Then CTA label shows 'Read More' rather than 'Download' to reflect article navigation

---
Feature: Resource access handoff without false download implication
  # issue_0033

  Scenario: eBook Download reaches resource detail flow
    Given A user clicks Download on an eBook card
    When Navigation completes
    Then The user reaches the resource detail/access flow rather than a direct file download

  Scenario: Implementation does not expose private asset endpoint
    Given eBook cards are implemented
    When Network traffic is analyzed
    Then Implementation does not fabricate or expose private asset URLs directly

  Scenario: Gated content communicates required steps clearly
    Given A resource requires gate/submission
    When The user reaches the gate
    Then The required steps are clearly communicated

  Scenario: Only verified destinations used for resources
    Given Resource cards are rendered
    When URL validation runs
    Then All resource URLs point to verified/published destinations
