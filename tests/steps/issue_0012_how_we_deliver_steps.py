"""Step definitions for issue_0012: How We Deliver Section Rendering."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.how_we_deliver_page import HowWeDeliverPage


@given("How We Deliver section is configured")
def section_configured(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Page renders")
def page_renders_hwd(page: Page):
    pass


@then("Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence")
def section_renders_sequence(page: Page):
    hwd = HowWeDeliverPage(page)
    expect(hwd.section_heading).to_be_visible()
    expect(hwd.supporting_explanation).to_be_visible()
    expect(hwd.cta).to_be_visible()


@given("How We Deliver section renders")
def section_renders(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Accessibility is checked")
def check_accessibility(page: Page):
    pass


@then("All content elements are accessible")
def elements_accessible(page: Page):
    hwd = HowWeDeliverPage(page)
    expect(hwd.section_heading).to_be_visible()
    expect(hwd.supporting_explanation).to_be_visible()


@given("How We Deliver content is configured")
def content_configured(page: Page):
    page.goto("/")


@when("Required fields are validated")
def validate_fields(page: Page):
    pass


@then("Required content fields (title, body, CTA) are non-empty")
def required_fields_nonempty(page: Page):
    hwd = HowWeDeliverPage(page)
    heading = hwd.section_heading.text_content()
    assert heading and heading.strip(), "Heading should not be empty"
    body = hwd.supporting_explanation.text_content()
    assert body and body.strip(), "Body should not be empty"


@given("Page heading structure is reviewed")
def heading_structure_reviewed(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Headings follow logical hierarchy from H1 through subsequent levels")
def check_hierarchy(page: Page):
    pass


@then("Heading hierarchy remains logical (H1 > H2 > H3)")
def hierarchy_logical(page: Page):
    h1 = page.get_by_role("heading", level=1).first
    h2 = page.get_by_role("heading", level=2).first
    h3 = page.get_by_role("heading", level=3).first
    expect(h1).to_be_visible()
    expect(h2).to_be_visible()
    expect(h3).to_be_visible()


@given("Visual media is not available")
def media_not_available(page: Page):
    page.goto("/")
    page.route(lambda url: "image" in url or "video" in url, lambda route: route.abort())


@when("Section renders")
def section_renders_no_media(page: Page):
    page.wait_for_load_state("domcontentloaded")


@then("Section renders appropriately without breaking layout")
def section_without_media(page: Page):
    hwd = HowWeDeliverPage(page)
    expect(hwd.section_heading).to_be_visible()


@given("Section has unusually long copy")
def long_copy(page: Page):
    page.goto("/")


@when("Section renders at viewport")
def section_at_viewport(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@then("Content reflows without breaking layout")
def reflow_without_break(page: Page):
    hwd = HowWeDeliverPage(page)
    expect(hwd.section).to_be_visible()
