"""Feature: Contact form functionality (emids_lp_047-049)."""
Feature: Contact form functionality

    @emids_lp_047 @contact
    Scenario: All required fields displayed on contact page
        Given User navigates to contact page
        When Form renders
        Then All fields present: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

    @emids_lp_047 @contact @accessibility
    Scenario: Labels associated with controls
        Given User examines form fields
        When User checks accessibility
        Then Each input has associated label
        And Screen reader can identify fields

    @emids_lp_047 @contact
    Scenario: Submission provides clear feedback
        Given User submits contact form
        When Submission completes
        Then Clear success or failure feedback displays

    @emids_lp_047 @contact
    Scenario: Required fields enforced
        Given User attempts to submit incomplete form
        When Submission triggers
        Then Required field validation messages display
        And Submission prevented

    @emids_lp_047 @contact
    Scenario: Email validation with valid syntax
        Given User enters invalid email format
        When User submits form
        Then Validation error indicates email format issue

    @emids_lp_048 @contact
    Scenario: Select contains approved options
        Given User views Inquiry Type field
        When User opens dropdown
        Then Options present: Services, Careers, Employment Verification, Media Request, Other

    @emids_lp_048 @contact
    Scenario: Valid choice required for required field
        Given Inquiry Type is marked required
        When User submits without selection
        Then Validation error
        And Placeholder 'Select...' not accepted

    @emids_lp_049 @contact
    Scenario: Submit enters pending state
        Given User clicks submit
        When Submission processing begins
        Then Submit button shows pending state
        And Feedback given

    @emids_lp_049 @contact
    Scenario: Duplicate activation prevented while pending
        Given Submission in progress
        When User clicks submit again
        Then Duplicate submission prevented
        And No additional request

    @emids_lp_049 @contact
    Scenario: Success announced
        Given Form submission succeeds
        When Server confirms success
        Then Success message announced
        And Accessible for screen readers

    @emids_lp_049 @contact
    Scenario: Failure keeps user content and permits retry
        Given Form submission fails
        When Error occurs
        Then User-entered content preserved
        And Retry option available
        And Clear error message
