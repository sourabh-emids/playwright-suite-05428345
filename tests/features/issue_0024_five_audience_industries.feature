"""Feature: Five Audience Industry Entries."""
Feature: Five Audience Industry Entries

  @issue_0024
  Scenario: all_five_audiences_visible
    Given Who We Serve section renders
    When Audiences are counted
    Then All five audiences (Payer, Provider, HealthTech, Life Sciences, Consumer) are visible

  @issue_0024
  Scenario: each_explore_routes_to_segment
    Given Each audience has Explore action
    When Explore is clicked
    Then Action routes to canonical segment page: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

  @issue_0024
  Scenario: explore_keyboard_touch_accessible
    Given Explore actions are rendered
    When User interacts via keyboard or touch
    Then Interactions work on keyboard and touch

  @issue_0024
  Scenario: exactly_five_audiences_for_content_version
    Given Audiences section is configured
    When Audience count is validated
    Then Exactly five current audiences exist for this content version

  @issue_0024
  Scenario: audience_canonical_urls
    Given Audience explore links are configured
    When URLs are validated
    Then All URLs are canonical

  @issue_0024
  Scenario: responsive_tabs_cards_rail
    Given Who We Serve section renders across viewports
    When Viewport changes
    Then Responsive tabs/cards/accordion/rail work without hiding access

  @issue_0024
  Scenario: one_segment_unavailable_handling
    Given One segment page is unavailable
    When Section renders
    Then Unavailable segment handled gracefully

  @issue_0024
  Scenario: tab_state_after_resize
    Given User selects an audience tab at desktop width
    When Viewport resizes to mobile
    Then Tab state is preserved or transitioned appropriately

  @issue_0025
  Scenario: all_four_metrics_visible_as_text
    Given Impact section renders
    When Metrics are checked
    Then All four value/label pairs are visible as text: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, 450+ Platforms Launched

  @issue_0025
  Scenario: values_understandable_without_animation
    Given Count-up animation is present but disabled or incomplete
    When User views metrics
    Then Values remain understandable without animation

  @issue_0025
  Scenario: screen_readers_receive_final_values
    Given Impact metrics render with animation
    When Screen reader interprets section
    Then Screen readers receive final meaningful values (not animation intermediate states)

  @issue_0025
  Scenario: values_labels_paired_content
    Given Impact metrics are managed
    When Values and labels are checked
    Then Values and labels are managed as paired content

  @issue_0025
  Scenario: currency_symbol_plus_sign_preserved
    Given Impact metrics contain currency symbols and plus signs
    When Metrics render
    Then Currency symbols and plus signs are preserved where approved

  @issue_0025
  Scenario: animation_disabled_handling
    Given Count-up animation is disabled via settings
    When Section renders
    Then Final values display correctly

  @issue_0025
  Scenario: locale_formatting_handling
    Given User locale differs from default
    When Metrics render
    Then Locale formatting is handled appropriately

  @issue_0026
  Scenario: six_insight_cards_render
    Given Insights section renders
    When Cards are counted
    Then Six cards render

  @issue_0026
  Scenario: cards_have_required_content
    Given Each insight card is reviewed
    When Content type, title, action are checked
    Then Each card has content type, title, image where configured, and Download/Read More action

  @issue_0026
  Scenario: cards_accessible_at_all_breakpoints
    Given Insights cards render across viewports
    When Viewport changes
    Then Cards remain accessible at all breakpoints

  @issue_0026
  Scenario: card_urls_canonical
    Given Insight cards are configured
    When URLs are validated
    Then URLs are canonical and resolve

  @issue_0026
  Scenario: card_cta_labels_match_content_flow
    Given Insight cards render
    When CTA labels are checked
    Then Action labels match content flow (Download for eBooks, Read More for articles)

  @issue_0026
  Scenario: resource_unpublished_handling
    Given One insight resource is unpublished
    When Section renders
    Then Unpublished resource handled gracefully

  @issue_0026
  Scenario: missing_image_card_handling
    Given Card has missing thumbnail image
    When Card renders
    Then Card renders appropriately without breaking layout

  @issue_0026
  Scenario: long_title_handling
    Given Card has unusually long title
    When Card renders at viewport
    Then Long title handled gracefully without breaking layout

  @issue_0027
  Scenario: medicare_ebook_title_correct
    Given Medicare Advantage eBook card renders
    When Title is checked
    Then Title displays as 'Managing the Margin Reset in Medicare Advantage'

  @issue_0027
  Scenario: medicare_ebook_type_correct
    Given Medicare Advantage eBook card renders
    When Type is checked
    Then Content type shows as eBook

  @issue_0027
  Scenario: medicare_ebook_download_action
    Given Medicare Advantage eBook card renders
    When Action is checked
    Then Download action is displayed and routes correctly

  @issue_0027
  Scenario: medicare_ebook_image_if_available
    Given Medicare Advantage eBook has imagery configured
    When Card renders
    Then Image displays where available

  @issue_0027
  Scenario: medicare_ebook_detail_url_resolves
    Given Medicare Advantage eBook CTA is clicked
    When Navigation completes
    Then User reaches detail/access page at /insights/managing-the-margin-reset-in-medicare-advantage/

  @issue_0027
  Scenario: medicare_ebook_resource_removed_handling
    Given Medicare Advantage resource is removed or gated differently
    When User accesses card
    Then Appropriate handling occurs

  @issue_0028
  Scenario: cms0057_card_title_populated
    Given CMS-0057 interoperability resource card renders
    When Title is checked
    Then Card title is populated from approved content

  @issue_0028
  Scenario: cms0057_card_type_action_populated
    Given CMS-0057 card renders
    When Type and action are checked
    Then Card type and action are populated from approved content

  @issue_0028
  Scenario: cms0057_card_navigates_correctly
    Given CMS-0057 card action is activated
    When Navigation completes
    Then User reaches intended resource destination

  @issue_0028
  Scenario: cms0057_no_empty_title
    Given CMS-0057 card is configured
    When Title is validated
    Then Title is not empty

  @issue_0028
  Scenario: cms0057_destination_available
    Given CMS-0057 destination is configured
    When URL is validated
    Then Destination resolves and is not empty

  @issue_0029
  Scenario: life_sciences_ebook_title_correct
    Given Life Sciences transformation eBook card renders
    When Title is checked
    Then Title displays as 'Unlocking Trusted Digital Transformation in Life Sciences'

  @issue_0029
  Scenario: life_sciences_ebook_download_action
    Given Life Sciences eBook card renders
    When Action is activated
    Then Download action opens correct detail/access experience

  @issue_0029
  Scenario: life_sciences_ebook_canonical_url
    Given Life Sciences eBook card routes
    When URL is validated
    Then Canonical detail URL is used: /insights/unlocking-trusted-digital-transformation-in-life-sciences/

  @issue_0029
  Scenario: life_sciences_ebook_resource_access_flow
    Given User clicks Download on Life Sciences eBook
    When Navigation completes
    Then User reaches resource detail/access flow

  @issue_0030
  Scenario: ai_roi_ebook_title_correct
    Given AI ROI eBook card renders
    When Title is checked
    Then Title displays as 'Closing the AI ROI Gap in Healthcare'

  @issue_0030
  Scenario: ai_roi_ebook_label_correct
    Given AI ROI eBook card renders
    When Type is checked
    Then Card is labeled as eBook

  @issue_0030
  Scenario: ai_roi_ebook_expected_action
    Given AI ROI eBook card renders
    When Action is checked
    Then Expected action is present and functional

  @issue_0030
  Scenario: ai_roi_ebook_published_content
    Given AI ROI eBook is configured
    When Content status is checked
    Then Content is published and URL is valid

  @issue_0031
  Scenario: finops_payer_card_title_action
    Given FinOps healthcare payer resource card renders
    When Title and action are checked
    Then Card displays title and routes correctly

  @issue_0031
  Scenario: finops_payer_valid_destination
    Given FinOps card action is activated
    When Navigation completes
    Then User reaches configured resource destination

  @issue_0031
  Scenario: finops_payer_card_type_correct
    Given FinOps payer resource card renders
    When Type is checked
    Then Card type matches resource category

  @issue_0031
  Scenario: finops_payer_broken_link_handling
    Given FinOps resource URL is broken
    When Card action is activated
    Then Appropriate error handling occurs

  @issue_0032
  Scenario: payer_data_blog_title_correct
    Given Payer data readiness blog card renders
    When Title is checked
    Then Title displays as 'Payers: Is Your Data Ready for AI?'

  @issue_0032
  Scenario: payer_data_blog_type_blog
    Given Payer data readiness card renders
    When Type is checked
    Then Content type is Blog

  @issue_0032
  Scenario: payer_data_blog_read_more_action
    Given Payer data readiness blog card renders
    When Action label is checked
    Then CTA shows 'Read More' (not Download)

  @issue_0032
  Scenario: payer_data_blog_correct_destination
    Given Read More action is activated
    When Navigation completes
    Then User reaches correct article/detail experience

  @issue_0032
  Scenario: payer_data_blog_cta_label_article_not_download
    Given Blog card action label is configured
    When Label is validated
    Then Label reflects article navigation rather than file download

  @issue_0033
  Scenario: download_reaches_resource_detail_flow
    Given User clicks Download on eBook card
    When Navigation completes
    Then User reaches resource detail/access flow (not direct file URL)

  @issue_0033
  Scenario: no_fabricated_private_asset_endpoints
    Given Resource cards are implemented
    When URLs are inspected
    Then Implementation does not fabricate or expose private asset endpoints

  @issue_0033
  Scenario: gate_communicates_required_steps
    Given Resource is gated
    When User reaches gate
    Then Gate clearly communicates required steps

  @issue_0033
  Scenario: only_verified_destinations_used
    Given Resource card destinations are configured
    When URLs are validated
    Then Only verified/published destinations are used

  @issue_0033
  Scenario: gated_asset_unavailable_handling
    Given Gated asset is unavailable
    When User attempts access
    Then Appropriate error handling occurs

  @issue_0033
  Scenario: popup_blocked_handling
    Given Popup is used for resource access and popup blocker is active
    When User activates access
    Then Graceful fallback handling occurs
