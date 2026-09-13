Feature: Contact form fields display
  # issue_0047

  Scenario: All required form fields displayed
    Given The contact page is loaded via Connect CTA
    When The form is rendered
    Then All fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, and Comments

  Scenario: Labels associated with controls
    Given The contact form is rendered
    When Accessibility testing runs
    Then All form labels are properly associated with their controls

  Scenario: Submission provides clear success failure feedback
    Given A user submits the contact form
    When Submission completes
    Then Clear success or failure feedback is displayed to the user

  Scenario: Required fields are enforced client-side
    Given The contact form is rendered
    When User attempts to submit without required fields
    Then Client-side validation prevents submission and highlights required fields

  Scenario: Email field requires valid syntax
    Given The contact form has an email field
    When User enters invalid email format
    Then Validation error occurs preventing submission

  Scenario: Server revalidates form submission
    Given A form submission is received
    When Server processes the request
    Then Server-side validation occurs even if client validation passed

---
Feature: Inquiry Type values on contact form
  # issue_0048

  Scenario: Select control contains approved options
    Given The contact form Inquiry Type field is rendered
    When Options are analyzed
    Then Options include: Services, Careers, Employment Verification, Media Request, and Other

  Scenario: Inquiry Type requires valid choice
    Given The Inquiry Type select is configured as required
    When User submits without selecting a value
    Then Validation error occurs

  Scenario: Placeholder is not a valid choice
    Given The Inquiry Type select has a 'Select...' placeholder
    When User submits with placeholder value
    Then Validation error occurs as placeholder is not a valid choice

  Scenario: Values outside enum are rejected
    Given An inquiry submission contains a tampered value
    When Server validates the request
    Then Values outside the allowed enum are rejected

---
Feature: Contact form submission feedback and retry
  # issue_0049

  Scenario: Submit enters pending state
    Given A user clicks submit on the contact form
    When Submission begins processing
    Then Form enters a pending state with appropriate visual feedback

  Scenario: Duplicate activation prevented while pending
    Given Form submission is in pending state
    When User attempts to submit again
    Then Duplicate submission is prevented

  Scenario: Success announced to user
    Given Form submission succeeds
    When Response is received
    Then Success message is announced via live region or visible feedback

  Scenario: Failure keeps user content and permits retry
    Given Form submission fails
    When Error response is received
    Then User-entered content is preserved and retry is permitted

  Scenario: Server errors map to fields where possible
    Given Server returns validation errors
    When Error response is processed
    Then Field-level errors are displayed next to relevant fields where applicable

  Scenario: Timeout handling preserves form state
    Given Form submission times out
    When Timeout error occurs
    Then User content is preserved and user is informed of the timeout

---
Feature: WCAG 2.1 AA compliance
  # issue_0050

  Scenario: Full keyboard access throughout page
    Given A user navigates the page using only keyboard
    When All interactive elements are tested
    Then All functionality is accessible via keyboard

  Scenario: Visible focus maintained on all elements
    Given Keyboard navigation is active
    When Focus moves between interactive elements
    Then Visible focus indicator is maintained

  Scenario: Semantic landmarks identified
    Given The page is analyzed by assistive technology
    When Landmarks are detected
    Then Main, header, nav, footer, and section landmarks are properly identified

  Scenario: Sufficient color contrast throughout
    Given Color contrast testing is performed
    When Text and interactive elements are analyzed
    Then Contrast ratios meet WCAG AA requirements (4.5:1 for normal text, 3:1 for large text)

  Scenario: Meaningful alt text on images
    Given Images are present on the page
    When Accessibility testing runs
    Then Images have meaningful alt text or are properly marked as decorative

  Scenario: Interactive elements have accessible names
    Given Buttons, links, and controls are present
    When Accessibility testing analyzes elements
    Then All interactive elements have accessible names

  Scenario: 200% zoom supported without horizontal scroll
    Given Browser zoom is set to 200%
    When The page renders
    Then Content reflows appropriately without requiring horizontal scrolling

  Scenario: Form errors properly associated
    Given Form validation errors exist
    When Screen reader testing runs
    Then Error messages are properly associated with their form fields

  Scenario: Reduced motion preference respected
    Given User has prefers-reduced-motion enabled
    When The page renders
    Then Animations are reduced or disabled

  Scenario: Media alternatives provided
    Given Video or audio content is present
    When Accessibility testing runs
    Then Captions, transcripts, or audio descriptions are available where applicable

  Scenario: Not relying on color alone for information
    Given Color is used to convey information
    When Visual inspection runs
    Then Information is not conveyed through color alone

  Scenario: Touch targets meet minimum size
    Given Interactive elements on touch devices
    When Touch target sizes are measured
    Then Touch targets meet minimum size requirements (at least 44x44 CSS pixels)

---
Feature: SEO metadata and crawlable structure
  # issue_0051

  Scenario: Page has unique title
    Given The page is rendered
    When SEO metadata is analyzed
    Then A unique title tag is present

  Scenario: Meta description present
    Given The page is rendered
    When SEO metadata is analyzed
    Then A meta description tag is present

  Scenario: Canonical URL set
    Given The page is rendered
    When Canonical link tag is analyzed
    Then Canonical URL points to the primary homepage URL

  Scenario: Primary text is server-rendered
    Given The page is tested by search engine crawlers
    When Content extraction occurs
    Then Primary text content is available without JavaScript execution

  Scenario: Social preview metadata configured
    Given The page is analyzed for social metadata
    When Open Graph and Twitter tags are checked
    Then Social preview metadata is configured with og:title, og:description, og:image where applicable

  Scenario: Headings reflect page topic
    Given The page heading structure is analyzed
    When SEO review runs
    Then H1 and subsequent headings reflect the page topic

  Scenario: No conflicting duplicate title tags
    Given The page is analyzed
    When Title tags are checked
    Then No duplicate or conflicting title tags exist

---
Feature: Responsive layout across viewports
  # issue_0052

  Scenario: No horizontal scrolling at any viewport
    Given The page is tested at 320px width
    When Layout is analyzed
    Then No unintended horizontal scrolling occurs

  Scenario: Typography readable at all breakpoints
    Given The page is tested at various viewport widths
    When Text content is reviewed
    Then Typography remains readable and appropriately sized

  Scenario: Controls do not overlap
    Given The page is tested at tablet and mobile widths
    When Layout is analyzed
    Then Interactive controls do not overlap each other

  Scenario: All cards and sections remain available
    Given The page is tested at various viewport widths
    When Content is reviewed
    Then All card and section content remains accessible

  Scenario: Images preserve aspect ratio
    Given Images are rendered at various viewport widths
    When Aspect ratios are measured
    Then Images maintain their intended aspect ratios

  Scenario: Content usable at 200% zoom
    Given Browser zoom is set to 200%
    When The page renders
    Then Content remains usable without breaking layout

  Scenario: Long text content handled appropriately
    Given Sections contain very long text content
    When The page renders at various widths
    Then Text reflows appropriately without breaking layout

  Scenario: Tablet split-screen handled
    Given Page is viewed in tablet split-screen mode
    When Layout is analyzed
    Then Content adapts appropriately to narrower viewport

---
Feature: Performance and Core Web Vitals
  # issue_0053

  Scenario: Critical content renders without waiting for analytics
    Given Third-party analytics scripts are configured
    When Page load is measured
    Then Critical content is available without waiting for analytics scripts to load

  Scenario: Images are sized and optimized
    Given Images are present on the page
    When Performance audit runs
    Then Images are appropriately sized and optimized for delivery

  Scenario: Below-fold media lazy-loaded appropriately
    Given Below-the-fold media is present
    When Performance testing runs
    Then Below-fold media uses lazy loading where appropriate

  Scenario: Layout shifts minimized
    Given The page is tested for stability
    When Core Web Vitals are measured
    Then Cumulative Layout Shift (CLS) is minimized

  Scenario: Third-party scripts use async defer consent gating
    Given Third-party scripts are configured
    When Script loading strategies are analyzed
    Then Scripts use async/defer attributes and consent gating as appropriate

  Scenario: Large unoptimized assets avoided
    Given Page assets are analyzed
    When Performance audit runs
    Then No large unoptimized assets are present

---
Feature: Script failure graceful handling
  # issue_0054

  Scenario: Header remains readable when optional scripts fail
    Given Optional analytics, consent, or marketing scripts fail
    When The page renders
    Then The global header remains visible and navigable

  Scenario: Main content accessible when scripts fail
    Given Optional third-party scripts fail
    When The page renders
    Then Main content remains accessible

  Scenario: CTAs functional when scripts fail
    Given Optional scripts fail to load
    When User attempts to click CTAs
    Then CTAs remain functional

  Scenario: Footer navigable when scripts fail
    Given Optional scripts fail to load
    When The page renders
    Then Footer remains navigable

  Scenario: Errors are contained and not fatal
    Given A third-party script fails
    When The error occurs
    Then Error is contained and does not break core functionality

  Scenario: Fallback content used when primary fails
    Given A script or asset fails
    When The page renders
    Then Fallback text or images are displayed where available

---
Feature: No unsolicited modal in base experience
  # issue_0055

  Scenario: Base homepage loads without unsolicited promotional modal
    Given The base homepage configuration is loaded
    When The page renders
    Then No promotional modal appears without user action

  Scenario: Campaign modal is separately governed
    Given A campaign modal is configured
    When The configuration is reviewed
    Then Campaign modal has separate governance including title, content, dismiss control, and activation rule

  Scenario: Configured modal is dismissible and keyboard accessible
    Given A campaign modal is configured and displayed
    When User interacts with the modal
    Then The modal is dismissible and keyboard accessible

  Scenario: Default state has modals disabled
    Given The homepage configuration is reviewed
    When Default settings are checked
    Then Default state has modals disabled
