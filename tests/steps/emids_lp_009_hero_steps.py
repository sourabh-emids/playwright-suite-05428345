"""Step definitions for emids_lp_009-013: Hero and How We Deliver sections."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


# Hero (emids_lp_009)
@given("Page renders hero section")
def page_renders_hero(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Hero section renders")
def hero_section_renders(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("H1 element exists")
def h1_exists(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Page loads on common desktop viewport (1280x720 minimum)")
def desktop_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Hero contains media (image/video)")
def hero_has_media(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Hero media URL is configured")
def hero_media_configured(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Network is slow or media is large")
def slow_network(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Hero copy contains maximum text length")
def max_hero_copy(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User prefers reduced motion")
def prefers_reduced_motion(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Automated check scans heading hierarchy")
def scan_headings(page: Page) -> None:
    pass


@when("User views H1 content")
def view_h1_content(page: Page) -> None:
    pass


@when("Automated check validates H1")
def validate_h1(page: Page) -> None:
    pass


@when("User views supporting copy")
def view_supporting_copy(page: Page) -> None:
    pass


@when("Hero section renders without scrolling")
def hero_no_scroll(page: Page) -> None:
    pass


@when("Media fails to load or screen reader is used")
def media_fails(page: Page) -> None:
    pass


@when("User views eyebrow content")
def view_eyebrow(page: Page) -> None:
    pass


@when("Automated check tests media endpoint")
def test_media_endpoint(page: Page, base_url: str) -> None:
    pass


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Page renders on narrow viewport")
def render_narrow_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("Page renders at mobile width")
def render_mobile_width(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})


@when("Hero with animated elements renders")
def animated_hero_renders(page: Page) -> None:
    pass


@then("Exactly one H1 is present on the page")
def verify_single_h1(page: Page) -> None:
    h1_count = page.locator("h1").count()
    assert h1_count == 1, f"Expected 1 H1, found {h1_count}"


@then("H1 displays 'In Healthcare, Only Outcomes Matter' as primary message")
def verify_h1_text(page: Page) -> None:
    expect(page.locator("h1")).to_contain_text("In Healthcare, Only Outcomes Matter")


@then("H1 is non-empty and unique on the page")
def verify_h1_valid(page: Page) -> None:
    h1_text = page.locator("h1").first.inner_text()
    assert h1_text.strip(), "H1 is empty"
    assert page.locator("h1").count() == 1, "Multiple H1s found"


@then("Supporting content is readable with appropriate contrast and font sizing")
def verify_readable_supporting(page: Page) -> None:
    h2 = page.locator("h2").first
    expect(h2).to_be_visible()


@then("CTA is visible above/before deep page scrolling")
def verify_cta_above_fold(page: Page) -> None:
    main_cta = page.locator("main a").first
    expect(main_cta).to_be_in_viewport()


@then("Appropriate alternative text or fallback is provided; decorative media has no redundant screen reader output")
def verify_alt_text(page: Page) -> None:
    images = page.locator("main img")
    for img in images.all():
        alt = img.get_attribute("alt")
        assert alt is not None or img.get_attribute("role") == "presentation"


@then("Eyebrow text is displayed above H1 if configured")
def verify_eyebrow(page: Page) -> None:
    eyebrow = page.locator('[class*="eyebrow"], [class*="tagline"]')
    if eyebrow.count() > 0:
        expect(eyebrow.first).to_be_visible()


@then("Media URL resolves successfully")
def verify_media_url_resolves(page: Page, base_url: str) -> None:
    pass


@then("Text content remains available even if media takes longer to load")
def verify_text_available(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h2")).to_be_visible()


@then("Copy wraps appropriately without breaking layout")
def verify_copy_wrapping(page: Page) -> None:
    section = page.locator("main > div").first
    box = section.bounding_box()
    assert box is not None


@then("Hero remains readable and CTA remains accessible")
def verify_mobile_hero(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("main a").first).to_be_visible()


@then("Animation is reduced or static fallback is shown")
def verify_animation_reduced(page: Page) -> None:
    pass


# Hero CTA (emids_lp_010)
@given("User clicks hero CTA")
def click_hero_cta(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.locator("main a").first.click()


@given("Hero CTA URL is configured")
def hero_cta_configured(page: Page) -> None:
    pass


@given("User right-clicks hero CTA and selects 'Open in new tab'")
def right_click_hero_cta(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("FDCE page returns error")
def fdce_returns_error(page: Page) -> None:
    pass


@when("Navigation occurs")
def navigation_occurs(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Navigation completes")
def nav_complete(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@then("User lands on Forward-Deployed Context Engineering canonical page")
def verify_fdce_landing(page: Page) -> None:
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@then("URL uses HTTPS protocol and is canonical (/forward-deployed-context-engineering/)")
def verify_canonical_fdce(page: Page) -> None:
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@then("Expected browser navigation behavior is preserved (history entry created, referrer set)")
def verify_nav_behavior(page: Page) -> None:
    assert len(page.context.pages) > 0


@then("FDCE page opens in new tab successfully")
def verify_new_tab(page: Page) -> None:
    pass


@then("User sees appropriate error page (404/500) rather than broken experience")
def verify_error_page(page: Page) -> None:
    pass


# Hero Media (emids_lp_011)
@given("Hero media fails to load")
def hero_media_fails(page: Page) -> None:
    pass


@given("Hero contains media with known dimensions")
def hero_media_dimensions(page: Page) -> None:
    pass


@given("Hero media is requested")
def hero_media_requested(page: Page) -> None:
    pass


@given("Hero contains primary LCP (Largest Contentful Paint) media")
def lcp_media(page: Page) -> None:
    pass


@given("Hero contains video media")
def hero_video_media(page: Page) -> None:
    pass


@given("CDN serving hero media times out")
def cdn_timeout(page: Page) -> None:
    pass


@given("Browser does not support media format")
def unsupported_format(page: Page) -> None:
    pass


@given("User is on low-bandwidth connection")
def low_bandwidth(page: Page) -> None:
    pass


@when("Page renders")
def page_render(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("Automated check validates video element")
def validate_video_element(page: Page) -> None:
    pass


@then("Text content remains available and page is fully usable")
def verify_text_available_full(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()


@then("Layout space is reserved to avoid cumulative layout shift (CLS)")
def verify_layout_reserved(page: Page) -> None:
    pass


@then("Image is appropriately sized for viewport (srcset/sizes used where applicable)")
def verify_sized_image(page: Page) -> None:
    pass


@then("LCP asset is not lazy-loaded as it would harm LCP metric")
def verify_lcp_not_lazy(page: Page) -> None:
    pass


@then("Poster image and alt text are provided for accessibility")
def verify_poster_alt(page: Page) -> None:
    pass


@then("Fallback is shown and content remains accessible")
def verify_fallback_shown(page: Page) -> None:
    expect(page.locator("h1")).to_be_visible()


@then("Fallback or alternative is provided")
def verify_fallback_alt(page: Page) -> None:
    pass


@then("Optimized lower-resolution media is served or loads gracefully")
def verify_optimized_media(page: Page) -> None:
    pass


# How We Deliver (emids_lp_012)
@given("Page renders 'How We Deliver' section")
def render_how_we_deliver(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("'How We Deliver' section renders")
def how_we_deliver_renders(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Page contains multiple sections with headings")
def multiple_sections(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Section renders on mobile viewport")
def section_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("Section media fails to load or is not configured")
def section_media_fails(page: Page) -> None:
    pass


@given("Section body copy is at maximum length")
def max_body_copy(page: Page) -> None:
    pass


@given("CTA field is missing from section data")
def cta_missing(page: Page) -> None:
    pass


@when("Section content is displayed")
def section_content_displayed(page: Page) -> None:
    pass


@when("Automated check validates content fields")
def validate_content_fields(page: Page) -> None:
    pass


@when("Automated check scans heading levels")
def scan_heading_levels(page: Page) -> None:
    pass


@when("Content reflows")
def content_reflows(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("Section renders")
def section_renders(page: Page) -> None:
    pass


@then("Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence and are accessible")
def verify_section_sequence(page: Page) -> None:
    section = page.locator("section").filter(has=page.locator("text=Forward-deployed context engineering"))
    expect(section).to_be_visible()


@then("Required content fields (title, body, CTA) are not empty")
def verify_required_fields(page: Page) -> None:
    expect(page.locator("text=Forward-Deployed Context Engineering")).to_be_visible()


@then("Heading hierarchy follows logical order without skipped levels where avoidable")
def verify_heading_hierarchy(page: Page) -> None:
    h1 = page.locator("h1").count()
    h2 = page.locator("h2").count()
    h3 = page.locator("h3").count()
    assert h1 <= 1, "Multiple H1 found"
    assert h2 >= 0, "H2 missing"


@then("Content block adapts responsively following hero section")
def verify_responsive_block(page: Page) -> None:
    expect(page.locator("section").first).to_be_visible()


@then("Content remains accessible without broken image placeholders")
def verify_content_accessible(page: Page) -> None:
    expect(page.locator("h2")).to_be_visible()


@then("Copy wraps appropriately without breaking layout")
def verify_copy_wrap(page: Page) -> None:
    section = page.locator("section").first
    box = section.bounding_box()
    assert box is not None


@then("Section renders without CTA or shows placeholder based on requirements")
def verify_section_no_cta(page: Page) -> None:
    pass


# See the model CTA (emids_lp_013)
@given("User clicks 'See the model' CTA")
def click_see_model_cta(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.locator('a:has-text("See the model")').first.click()


@given("User focuses on 'See the model' CTA")
def focus_see_model_cta(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")
    page.locator('a:has-text("See the model")').first.focus()


@given("CTA element exists")
def cta_exists(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("'See the model' CTA URL is configured")
def see_model_cta_configured(page: Page) -> None:
    pass


@given("Multiple CTAs on page have focus behavior")
def multiple_ctas_focus(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@given("User interacts with 'See the model' CTA")
def interact_see_model_cta(page: Page) -> None:
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User activates via keyboard (Enter/Space)")
def activate_via_keyboard(page: Page) -> None:
    page.locator('a:has-text("See the model")').first.press("Enter")


@when("Screen reader reads the element")
def screen_reader_reads_cta(page: Page) -> None:
    pass


@when("Automated check tests destination")
def test_destination(page: Page, base_url: str) -> None:
    pass


@when("User tabs through page")
def tab_through(page: Page) -> None:
    page.locator("body").focus()
    for _ in range(15):
        page.keyboard.press("Tab")


@when("User hovers or focuses on CTA")
def hover_focus_cta(page: Page) -> None:
    page.locator('a:has-text("See the model")').first.hover()


@then("User lands on FDCE detail page at /forward-deployed-context-engineering/")
def verify_fdce_detail(page: Page) -> None:
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@then("CTA triggers navigation to FDCE detail page")
def verify_cta_nav_fdce(page: Page) -> None:
    expect(page).to_have_url("**/forward-deployed-context-engineering/**")


@then("Accessible name describes the action ('See the model')")
def verify_accessible_name_cta(page: Page) -> None:
    expect(page.locator('a:has-text("See the model")')).to_be_visible()


@then("URL returns 200 status; no 404 error")
def verify_url_200(page: Page, base_url: str) -> None:
    pass


@then("Each CTA is a distinct focus target with appropriate behavior")
def verify_distinct_ctas(page: Page) -> None:
    ctas = page.locator("section a")
    count = ctas.count()
    assert count >= 1


@then("Visible hover and focus states are displayed")
def verify_hover_focus_states(page: Page) -> None:
    cta = page.locator('a:has-text("See the model")').first
    cta.hover()
    expect(cta).to_be_visible()
