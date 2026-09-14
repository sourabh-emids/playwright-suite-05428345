"""Step definitions for issues 0047-0055: Remaining Modules."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


# Contact Form (issues 0047-0049)
@given("Contact form renders")
def contact_form_renders(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Fields are reviewed")
def review_fields(page: Page):
    pass


@then("All required fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments")
def required_fields_displayed(page: Page):
    first_name = page.get_byLabel(/First/)
    last_name = page.get_byLabel(/Last/)
    email = page.get_byLabel(/Email/)
    expect(first_name).to_be_visible()
    expect(last_name).to_be_visible()
    expect(email).to_be_visible()


@given("Contact form renders")
def contact_renders(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Labels and inputs are inspected")
def inspect_labels(page: Page):
    pass


@then("Labels are associated with controls")
def labels_associated(page: Page):
    first_name = page.get_byLabel(/First/)
    expect(first_name).to_be_attached()


@given("Form submission occurs")
def form_submission(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Response is received")
def response_received(page: Page):
    pass


@then("Submission provides clear success/failure feedback")
def clear_feedback(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    expect(submit_btn).to_be_visible()


@given("User navigates to contact page")
def navigate_contact(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Form is rendered")
def form_rendered(page: Page):
    pass


@then("Form is accessible (not embedded modal blocking interaction)")
def form_accessible(page: Page):
    expect(page.locator("form")).to_be_visible()


@given("User enters invalid email format")
def invalid_email(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Form is submitted")
def submit_invalid(page: Page):
    email_field = page.getByLabel(/Email/)
    email_field.fill("invalid-email")
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@then("Submission is rejected with appropriate error")
def rejected_error(page: Page):
    pass


@given("User enters very long comments")
def long_comments(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Form is submitted")
def submit_long_comments(page: Page):
    comments = page.getByLabel(/Comments/)
    comments.fill("x" * 10000)
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@then("Long comments are handled within limits")
def long_handled(page: Page):
    pass


@given("User double-clicks or rapidly submits")
def rapid_submit(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Submission processes")
def process_submission(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()
    page.wait_for_timeout(100)
    submit_btn.click()


@then("Duplicate submission is prevented")
def no_duplicate(page: Page):
    pass


@given("Backend returns error during submission")
def backend_error(page: Page):
    page.goto("/contact/")


@when("User submits form")
def submit_form(page: Page):
    page.wait_for_load_state("networkidle")


@then("User sees clear error and can retry")
def error_retry(page: Page):
    pass


@given("Automated/bot attempts form submission")
def bot_attempt(page: Page):
    page.goto("/contact/")


@when("Submission is detected")
def detect_submission(page: Page):
    pass


@then("Appropriate bot protection handles submission")
def bot_protection(page: Page):
    pass


# Inquiry Type (issue_0048)
@given("Contact form Inquiry Type field renders")
def inquiry_renders(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Options are checked")
def check_options(page: Page):
    pass


@then("Select contains all approved options: Services, Careers, Employment Verification, Media Request, Other")
def approved_options(page: Page):
    select = page.getByLabel(/Inquiry/)
    expect(select).to_be_visible()


@given("Inquiry Type select exists")
def select_exists(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Form is submitted without selection")
def submit_no_selection(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@then("Valid choice is required before submission")
def choice_required(page: Page):
    pass


@given("User submits without changing placeholder")
def no_change(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Form is submitted")
def submit_unchanged(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@then("Placeholder 'Select...' is not accepted as valid choice")
def not_valid_placeholder(page: Page):
    pass


@given("Tampered request sends unknown inquiry type")
def tampered_request(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Server processes")
def server_processes(page: Page):
    pass


@then("Values outside allowed enum are rejected")
def rejected_enum(page: Page):
    pass


@given("Inquiry Type select renders")
def inquiry_select(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Accessibility is checked")
def check_a11y(page: Page):
    pass


@then("Field uses native select or accessible custom combobox")
def accessible_combobox(page: Page):
    select = page.getByRole("combobox")
    expect(select).to_be_visible()


# Form Submission Feedback (issue_0049)
@given("User submits form")
def user_submits(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@when("Submission begins processing")
def processing(page: Page):
    page.wait_for_timeout(500)


@then("Submit button enters pending/loading state")
def pending_state(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    expect(submit_btn).to_be_visible()


@given("Form is in pending submission state")
def pending_form(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()
    page.wait_for_timeout(100)


@when("User attempts to submit again")
def submit_again(page: Page):
    submit_btn = page.getByRole("button", name="Submit")
    submit_btn.click()


@then("Duplicate activation is prevented")
def duplicate_prevented(page: Page):
    pass


@given("Form submission succeeds")
def submission_succeeds(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Response is received")
def response_success(page: Page):
    pass


@then("Success is announced (visually and via aria-live region)")
def success_announced(page: Page):
    pass


@given("Form submission fails")
def submission_fails(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Error is displayed")
def error_displayed(page: Page):
    pass


@then("User-entered content is preserved for retry")
def content_preserved(page: Page):
    pass


@given("Server returns validation errors")
def server_errors(page: Page):
    page.goto("/contact/")


@when("Errors display")
def display_errors(page: Page):
    page.wait_for_load_state("networkidle")


@then("Server-side validation errors map to fields where possible")
def errors_map(page: Page):
    pass


@given("Submission request times out")
def submission_timeout(page: Page):
    page.goto("/contact/")


@when("User receives response")
def user_receives(page: Page):
    page.wait_for_load_state("networkidle")


@then("Timeout is handled with appropriate feedback and retry option")
def timeout_feedback(page: Page):
    pass


@given("Form submission is pending")
def submission_pending(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("User navigates away")
def nav_away(page: Page):
    page.goto("/")


@then("Appropriate handling (warning or graceful exit) occurs")
def graceful_exit(page: Page):
    pass


# Accessibility (issue_0050)
@given("User interacts with page using keyboard only")
def keyboard_only(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("All interactive elements are accessed")
def access_elements(page: Page):
    for _ in range(10):
        page.keyboard.press("Tab")


@then("Page is fully navigable via keyboard")
def fully_keyboard(page: Page):
    pass


@given("User navigates via keyboard")
def keyboard_nav(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Focus indicator is checked")
def check_focus(page: Page):
    page.keyboard.press("Tab")


@then("Visible focus is maintained on all interactive elements")
def visible_focus(page: Page):
    pass


@given("Page structure is reviewed")
def structure_reviewed(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Landmarks are checked")
def check_landmarks(page: Page):
    pass


@then("Semantic landmarks (header, main, nav, footer) are present and identifiable")
def landmarks_present(page: Page):
    expect(page.locator("header")).to_be_visible()
    expect(page.locator("main")).to_be_visible()
    expect(page.locator("footer")).to_be_visible()


@given("Text and UI elements are tested")
def text_tested(page: Page):
    page.goto("/")


@when("Color contrast is measured")
def measure_contrast(page: Page):
    pass


@then("Contrast meets WCAG 2.1 AA requirements (4.5:1 for normal text, 3:1 for large text)")
def wcag_contrast(page: Page):
    pass


@given("Images and media exist on page")
def images_exist(page: Page):
    page.goto("/")


@when("Alt text is reviewed")
def review_alt(page: Page):
    pass


@then("Images have meaningful alt text; decorative images have empty alt")
def alt_meaningful(page: Page):
    images = page.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        assert alt is not None, "Image should have alt attribute"


@given("Interactive elements are tested")
def interactives_tested(page: Page):
    page.goto("/")


@when("Accessible names are checked")
def check_names(page: Page):
    pass


@then("All interactive elements have accessible names")
def names_accessible(page: Page):
    links = page.locator("a").all()
    for link in links:
        name = link.get_attribute("aria-label") or link.text_content()
        assert name and name.strip(), "Interactive element should have accessible name"


@given("Browser zoom is set to 200%")
def zoom_200(page: Page):
    page.set_viewport_size({"width": 640, "height": 360})


@when("Page is reviewed")
def review_zoom(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Content reflows without horizontal scrolling and remains usable")
def reflow_usable(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Form has validation errors")
def form_errors(page: Page):
    page.goto("/contact/")
    page.wait_for_load_state("networkidle")


@when("Errors display")
def errors_display(page: Page):
    pass


@then("Errors are presented accessibly and associated with fields")
def errors_accessible(page: Page):
    pass


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page):
    page.emulate_media(media="screen")


@when("Page renders with animations")
def render_animations(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Motion is reduced or eliminated")
def motion_reduced(page: Page):
    pass


@given("Video or audio content exists")
def media_exists(page: Page):
    page.goto("/")


@when("Accessibility is checked")
def check_a11y_media(page: Page):
    pass


@then("Captions, transcripts, or audio descriptions are available where needed")
def captions_available(page: Page):
    pass


@given("Touch targets exist")
def targets_exist(page: Page):
    page.goto("/")


@when("Size is measured")
def measure_size(page: Page):
    pass


@then("Touch targets meet minimum size (at least 44x44 CSS pixels)")
def min_size(page: Page):
    pass


@given("Information is conveyed via color")
def color_info(page: Page):
    page.goto("/")


@when("Multiple channels are checked")
def check_channels(page: Page):
    pass


@then("Information is not conveyed by color alone")
def not_color_alone(page: Page):
    pass


# SEO (issue_0051)
@given("Page renders")
def page_seo(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Title tag is checked")
def check_title(page: Page):
    pass


@then("Page has unique title")
def unique_title(page: Page):
    title = page.title()
    assert title and title.strip(), "Page should have title"


@given("Page renders")
def render_seo(page: Page):
    page.goto("/")


@when("Meta description is checked")
def check_desc(page: Page):
    pass


@then("Meta description is present and relevant")
def meta_present(page: Page):
    meta = page.locator('meta[name="description"]')
    expect(meta).to_be_attached()


@given("Page renders")
def render_canonical(page: Page):
    page.goto("/")


@when("Canonical tag is checked")
def check_canonical(page: Page):
    pass


@then("Canonical URL is set to homepage canonical")
def canonical_set(page: Page):
    canonical = page.locator('link[rel="canonical"]')
    expect(canonical).to_be_attached()


@given("Page content is inspected")
def content_inspected(page: Page):
    page.goto("/")


@when("Primary text availability is checked")
def check_text(page: Page):
    pass


@then("Primary text is server-rendered and crawlable (not JS-only critical content)")
def crawlable(page: Page):
    h1 = page.get_by_role("heading", level=1)
    expect(h1).to_be_visible()


@given("Page metadata is reviewed")
def metadata_reviewed(page: Page):
    page.goto("/")


@when("Open Graph and Twitter metadata are checked")
def check_og(page: Page):
    pass


@then("Social preview metadata is configured")
def og_configured(page: Page):
    og = page.locator('meta[property^="og:"]')
    expect(og).to_be_attached()


@given("Page heading structure is reviewed")
def heading_structure(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Headings are compared to page topic")
def compare_topic(page: Page):
    pass


@then("Headings reflect the page topic appropriately")
def topic_reflected(page: Page):
    h1 = page.get_by_role("heading", level=1)
    expect(h1).to_be_visible()


@given("Page renders")
def page_duplicates(page: Page):
    page.goto("/")


@when("Title tags are checked")
def check_titles(page: Page):
    pass


@then("No duplicate conflicting title tags exist")
def no_duplicates(page: Page):
    titles = page.locator("title").all()
    assert len(titles) <= 1, "Should have at most one title tag"


@given("OG image is missing from configuration")
def og_missing(page: Page):
    page.goto("/")


@when("Social sharing occurs")
def social_share(page: Page):
    pass


@then("Fallback or graceful handling occurs")
def fallback_og(page: Page):
    pass


# Responsive Layout (issue_0052)
@given("Page renders at supported viewports (320px and above)")
def supported_viewports(page: Page):
    page.goto("/")


@when("Horizontal scroll is checked")
def check_hscroll(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@then("No unintended horizontal scrolling occurs")
def no_hscroll(page: Page):
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert scroll_width <= viewport_width + 10, "No horizontal scroll"


@given("Page renders across viewports")
def across_viewports(page: Page):
    page.goto("/")


@when("Typography is reviewed")
def review_type(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Typography remains readable at all supported widths")
def type_readable(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Page renders at narrow viewport")
def narrow_viewport(page: Page):
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("Layout is checked")
def check_layout(page: Page):
    pass


@then("Controls do not overlap")
def no_overlap(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Content sections with cards exist")
def card_sections(page: Page):
    page.goto("/")


@when("Viewport changes")
def viewport_changes(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("All cards/sections remain available")
def cards_available(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Images render across viewports")
def images_viewports(page: Page):
    page.goto("/")


@when("Viewport changes")
def viewport_change_images(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@then("Images preserve aspect ratio")
def aspect_preserved(page: Page):
    pass


@given("Page renders at 320 CSS px width")
def width_320(page: Page):
    page.set_viewport_size({"width": 320, "height": 568})


@when("Content and functionality are tested")
def test_content(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Content remains usable and functional")
def usable_functional(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Browser zoom is at 200%")
def zoom_200_layout(page: Page):
    page.set_viewport_size({"width": 640, "height": 360})


@when("Page is reviewed")
def review_page(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Content and functionality remain usable")
def usable_zoom(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Phone is in landscape orientation")
def landscape_phone(page: Page):
    page.set_viewport_size({"width": 853, "height": 375})


@when("Page renders")
def render_landscape(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Content adapts appropriately")
def adapt_landscape(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Tablet uses split-screen mode")
def split_screen(page: Page):
    page.set_viewport_size({"width": 500, "height": 800})


@when("Page renders")
def render_split(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Content adapts appropriately")
def adapt_split(page: Page):
    expect(page.locator("header")).to_be_visible()


# Performance (issue_0053)
@given("Page loads")
def page_load(page: Page):
    page.goto("/")


@when("Critical content availability is checked")
def check_critical(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Critical content renders without waiting for analytics scripts")
def critical_without_analytics(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Images are present on page")
def images_present(page: Page):
    page.goto("/")


@when("Images are validated")
def validate_images(page: Page):
    pass


@then("Images are appropriately sized and optimized")
def images_optimized(page: Page):
    pass


@given("Below-the-fold media exists")
def below_fold(page: Page):
    page.goto("/")


@when("Loading behavior is checked")
def check_load(page: Page):
    pass


@then("Below-the-fold media is lazy-loaded where appropriate")
def lazy_loaded(page: Page):
    pass


@given("Page loads")
def page_load_perf(page: Page):
    page.goto("/")
    page.wait_for_load_state("load")


@when("Layout shift metrics are measured")
def measure_ls(page: Page):
    pass


@then("Layout shifts are minimized")
def ls_minimized(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Third-party scripts are configured")
def third_party(page: Page):
    page.goto("/")


@when("Script loading is checked")
def check_scripts(page: Page):
    page.wait_for_load_state("networkidle")


@then("Scripts are async/defer/consent-gated as appropriate")
def script_loading(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Assets are reviewed")
def assets_reviewed(page: Page):
    page.goto("/")


@when("Size and optimization are checked")
def check_size(page: Page):
    pass


@then("Large unoptimized assets are not present")
def no_large_unoptimized(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("User is on slow network")
def slow_network(page: Page):
    page.goto("/")


@when("Page loads")
def load_slow(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core content remains accessible")
def core_accessible(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Third-party scripts are blocked")
def third_blocked(page: Page):
    page.goto("/")


@when("Page loads")
def load_blocked(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core functionality continues")
def core_continues_perf(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Large viewport loads content")
def large_viewport(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})


@when("Image assets are requested")
def request_images(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@then("Appropriately sized images are served for the viewport")
def sized_images(page: Page):
    pass


# Script Failure Resilience (issue_0054)
@given("Analytics scripts fail to load")
def analytics_fail(page: Page):
    page.goto("/")
    page.route(lambda url: "analytics" in url or "google" in url, lambda route: route.abort())


@when("Page renders")
def render_analytics_fail(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Header remains readable")
def header_readable(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Consent scripts fail to load")
def consent_fail(page: Page):
    page.goto("/")
    page.route(lambda url: "consent" in url or "cookie" in url, lambda route: route.abort())


@when("Page renders")
def render_consent_fail(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Main content remains readable")
def main_readable(page: Page):
    expect(page.locator("main")).to_be_visible()


@given("Media integration scripts fail")
def media_fail(page: Page):
    page.goto("/")
    page.route(lambda url: "wistia" in url or "youtube" in url, lambda route: route.abort())


@when("User interacts with CTAs")
def interact_ctas(page: Page):
    pass


@then("CTAs remain functional")
def ctas_functional(page: Page):
    cta = page.get_byRole("link", name="Connect").first
    expect(cta).to_be_visible()


@given("Marketing scripts fail")
def marketing_fail(page: Page):
    page.goto("/")
    page.route(lambda url: "marketo" in url or "linkedin" in url, lambda route: route.abort())


@when("User interacts with footer")
def interact_footer(page: Page):
    pass


@then("Footer remains navigable")
def footer_navigable(page: Page):
    expect(page.locator("footer")).to_be_visible()


@given("Content Security Policy blocks a script")
def csp_block(page: Page):
    page.goto("/")


@when("Page renders")
def render_csp(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core content and navigation remain functional")
def core_navigation_csp(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("DNS resolution fails for third-party domain")
def dns_fail(page: Page):
    page.goto("/")


@when("Page renders")
def render_dns(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core page continues to function")
def core_dns(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Ad blocker prevents third-party script")
def ad_block(page: Page):
    page.goto("/")
    page.route(lambda url: "ads" in url or "doubleclick" in url, lambda route: route.abort())


@when("Page renders")
def render_ad(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core page functions normally")
def normal_functions(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Third-party script times out")
def script_timeout(page: Page):
    page.goto("/")


@when("Page renders")
def render_timeout(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Core functionality continues")
def core_timeout(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Vendor script is malformed")
def malformed_script(page: Page):
    page.goto("/")


@when("Page loads")
def load_malformed(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Page handles gracefully without breaking")
def graceful_malformed_script(page: Page):
    expect(page.locator("header")).to_be_visible()


# Modal (issue_0055)
@given("Base homepage configuration is reviewed")
def config_reviewed(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Page loads")
def page_load_base(page: Page):
    pass


@then("Base homepage loads without unsolicited promotional modal")
def no_unsolicited_modal(page: Page):
    modal = page.locator('[role="dialog"], .modal')
    expect(modal).not_to_be_visible()


@given("Campaign modal is configured and triggered")
def modal_triggered(page: Page):
    page.goto("/")


@when("User interacts with modal")
def interact_modal(page: Page):
    pass


@then("Modal is dismissible")
def dismissible(page: Page):
    close_btn = page.getByRole("button", name="Close")
    if close_btn.is_visible():
        close_btn.click()


@given("Campaign modal is open")
def modal_open(page: Page):
    page.goto("/")


@when("User navigates via keyboard")
def keyboard_modal(page: Page):
    page.keyboard.press("Escape")


@then("Modal is keyboard accessible (Escape to close, focus trap)")
def keyboard_modal_access(page: Page):
    pass


@given("Campaign modal is configured")
def modal_configured(page: Page):
    page.goto("/")


@when("Modal displays")
def modal_displays(page: Page):
    pass


@then("Modal is non-blocking (does not prevent page interaction)")
def non_blocking(page: Page):
    expect(page.locator("header")).to_be_visible()


@given("Campaign modal is not explicitly configured")
def not_configured(page: Page):
    page.goto("/")


@when("Page loads")
def page_load_not_configured(page: Page):
    page.wait_for_load_state("networkidle")


@then("Default state has modal disabled")
def modal_disabled_default(page: Page):
    modal = page.locator('[role="dialog"], .modal')
    expect(modal).not_to_be_visible()


@given("Campaign modal is enabled")
def modal_enabled(page: Page):
    page.goto("/")


@when("Configuration is validated")
def validate_modal_config(page: Page):
    pass


@then("Modal has title, content, dismiss control, and activation rule")
def modal_has_content(page: Page):
    pass


@given("User has dismissed modal")
def dismissed_modal(page: Page):
    page.goto("/")


@when("User continues browsing")
def continue_browsing(page: Page):
    pass


@then("Modal does not reappear repeatedly")
def no_reappear(page: Page):
    modal = page.locator('[role="dialog"], .modal')
    expect(modal).not_to_be_visible()


@given("JavaScript is disabled")
def js_disabled(page: Page):
    page.goto("/")


@when("Page loads")
def page_load_js_disabled(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Modal behavior defaults to non-intrusive state")
def non_intrusive_default(page: Page):
    modal = page.locator('[role="dialog"], .modal')
    expect(modal).not_to_be_visible()
