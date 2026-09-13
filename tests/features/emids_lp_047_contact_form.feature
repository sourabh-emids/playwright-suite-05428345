Feature: Contact form with all required fields

    @emids_lp_047
    Scenario: verify_all_required_fields_displayed
        Given Contact form renders
        When User views form
        Then All required fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

    @emids_lp_047
    Scenario: verify_labels_associated_with_controls
        Given Contact form renders
        When Screen reader or automated check validates
        Then Labels are properly associated with form controls

    @emids_lp_047
    Scenario: verify_required_field_enforcement
        Given User submits form without filling required fields
        When Submission is attempted
        Then Form returns validation errors requiring field completion

    @emids_lp_047
    Scenario: verify_email_validation
        Given User enters invalid email format
        When Form validates email field
        Then Validation error indicates invalid email syntax

    @emids_lp_047
    Scenario: verify_server_revalidation
        Given Form passes client validation
        When Form is submitted
        Then Server revalidates all fields

    @emids_lp_047
    Scenario: verify_clear_success_failure_feedback
        Given User submits contact form
        When Submission completes
        Then Clear success or failure feedback is provided

    @emids_lp_047
    Scenario: verify_accessible_form_on_contact_page
        Given Contact page renders
        When User or accessibility tool validates
        Then Form is accessible and not embedded inappropriately on homepage

    @emids_lp_047
    Scenario: verify_invalid_email_handling
        Given User submits with invalid email
        When Server validates
        Then Appropriate error message; form remains usable

    @emids_lp_047
    Scenario: verify_long_comments_handling
        Given User enters very long comments
        When Form submits or validates
        Then Input is handled gracefully with appropriate limits

    @emids_lp_047
    Scenario: verify_duplicate_submit_prevention
        Given User double-clicks submit
        When First submission in progress
        Then Duplicate submission is prevented

    @emids_lp_047
    Scenario: verify_timeout_handling
        Given Form submission times out
        When Server does not respond
        Then User sees timeout error with retry option

    @emids_lp_047
    Scenario: verify_backend_error_handling
        Given Backend returns error
        When Form is submitted
        Then User sees error message; form remains with content

    @emids_lp_047
    Scenario: verify_bot_submission_handling
        Given Automated bot submits form
        When Submission is detected as bot
        Then Appropriate handling (rejection, captcha, etc.)
