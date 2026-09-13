Feature: Support Inquiry Type values

    @emids_lp_048
    Scenario: verify_inquiry_type_options_present
        Given Inquiry Type field renders
        When User views select options
        Then Options include: Services, Careers, Employment Verification, Media Request, Other

    @emids_lp_048
    Scenario: verify_select_requires_valid_choice
        Given Inquiry Type is marked required
        When User submits without selection
        Then Validation error requires valid choice

    @emids_lp_048
    Scenario: verify_placeholder_not_valid_submission
        Given User selects 'Select...' placeholder
        When Form is submitted
        Then Placeholder is not accepted as valid choice; error shown

    @emids_lp_048
    Scenario: verify_reject_unknown_values
        Given Tampered request submits unknown Inquiry Type
        When Server validates
        Then Values outside allowed enum are rejected

    @emids_lp_048
    Scenario: verify_native_or_custom_combobox
        Given Inquiry Type field renders
        When User interacts with field
        Then Native select or accessible custom combobox is used

    @emids_lp_048
    Scenario: verify_option_removed_cached_form
        Given An Inquiry Type option is removed
        When Form is cached on user device
        Then System handles gracefully if removed option is submitted
