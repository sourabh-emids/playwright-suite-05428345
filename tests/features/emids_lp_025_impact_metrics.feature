Feature: Render Impact proof metrics

    @emids_lp_025
    Scenario: verify_all_four_metrics_visible
        Given Impact section renders
        When User views metrics
        Then All four metrics display: 36+ Years Healthcare Experience, 115+ Million Lives Touched, $48+ Billion Medical Costs Saved, 450+ Platforms Launched

    @emids_lp_025
    Scenario: verify_values_visible_as_text
        Given Impact metrics render
        When User views metric values
        Then All four values are visible as text (not hidden in images)

    @emids_lp_025
    Scenario: verify_values_readable_without_animation
        Given Count-up animation is configured
        When Animation is disabled or fails
        Then Final values remain understandable to users and screen readers

    @emids_lp_025
    Scenario: verify_screen_reader_final_values
        Given Metrics include count-up animation
        When Screen reader interprets content
        Then Screen readers receive final meaningful values

    @emids_lp_025
    Scenario: verify_values_labels_paired_content
        Given Impact metrics data
        When Automated check validates pairing
        Then Values and labels are managed as paired content

    @emids_lp_025
    Scenario: verify_currency_symbol_plus_sign_preserved
        Given Metric values include $ and + symbols
        When Metrics render
        Then Currency symbols and plus signs are preserved where approved

    @emids_lp_025
    Scenario: verify_animation_disabled_handling
        Given User has prefers_reduced_motion enabled
        When Impact metrics render with animation
        Then Animation is disabled; static final values display immediately

    @emids_lp_025
    Scenario: verify_locale_formatting
        Given Metric values render across different locales
        When Page loads in various locales
        Then Values format appropriately for locale without breaking layout

    @emids_lp_025
    Scenario: verify_cms_field_missing_handling
        Given One metric value field is missing in CMS
        When Section renders
        Then Validation catches missing field or graceful placeholder shown
