"""Feature: Render Impact proof metrics (emids_lp_025)."""
Feature: Render Impact proof metrics

    @emids_lp_025 @impact
    Scenario: All four value-label pairs visible as text
        Given User views Impact section
        When User reads metrics
        Then All four visible: '36+ Years Healthcare Experience', '115+ Million Lives Touched', '$48+ Billion Medical Costs Saved', '450+ Platforms Launched'

    @emids_lp_025 @impact
    Scenario: Values understandable without animation
        Given User views Impact section with animation disabled
        When Page renders
        Then Final metric values are readable and meaningful

    @emids_lp_025 @impact @accessibility
    Scenario: Screen readers receive final meaningful values
        Given User with screen reader views Impact section
        When Screen reader announces content
        Then Final metric values are read
        And Animation does not obscure values

    @emids_lp_025 @impact
    Scenario: Currency symbol and plus sign preserved
        Given User views Impact metrics
        When User reads values
        Then Approved formatting ($, +, etc.) displays correctly

    @emids_lp_025 @impact
    Scenario: Values and labels paired correctly
        Given CMS manages Impact content
        When Content renders
        Then Each value pairs correctly with its label
        And No mismatched pairings

    @emids_lp_025 @impact
    Scenario: Animation disabled environment
        Given Count-up animation fails or is disabled
        When Page renders
        Then Static values display correctly
        And No blank or loading state

    @emids_lp_025 @impact
    Scenario: Locale formatting handling
        Given User views page from different locale
        When Metrics render
        Then Values display with approved formatting
        And No unexpected locale transformation
