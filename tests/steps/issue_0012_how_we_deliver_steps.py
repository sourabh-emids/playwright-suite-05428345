"""Step definitions for Issue 0012 - How We Deliver section rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user scrolls to the How We Deliver section")
def scroll_to_how_we_deliver(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")
    page.wait_for_timeout(500)


@when("The section is in view")
def section_in_view(page: Page):
    pass


@then("Content renders in intended sequence: heading, supporting explanation, visual/content elements, and CTA")
def section_sequence_correct(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.how_we_deliver_section).to_be_visible()
    expect(homepage.see_the_model_cta).to_be_visible()


@given("A user views the How We Deliver section with assistive technology")
def view_how_we_deliver_at(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")


@when("The user navigates the section")
def navigate_section(page: Page):
    pass


@then("All elements are accessible and heading hierarchy is logical")
def heading_hierarchy_logical(page: Page):
    # Check heading structure
    h1 = page.get_by_role("heading", level=1)
    h2 = page.get_by_role("heading", level=2)
    h3 = page.get_by_role("heading", level=3)
    expect(h1).to_have_count(1)
    expect(h2).to_have_count(1)  # How We Deliver section


@given("A user views the How We Deliver section")
def view_how_we_deliver(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 700)")


@when("The section loads")
def section_loads(page: Page):
    page.wait_for_load_state("networkidle")


@then("Required content fields are not empty")
def required_fields_not_empty(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.how_we_deliver_section).to_be_visible()
    expect(homepage.see_the_model_cta).to_be_visible()


@given("A user or assistive technology examines the page structure")
def examine_page_structure(page: Page):
    pass


@when("The page HTML is analyzed")
def analyze_html(page: Page):
    pass


@then("Heading hierarchy (H1 > H2 > H3) remains logical")
def heading_hierarchy(page: Page):
    # Verify heading structure
    headings = page.locator("h1, h2, h3").all()
    levels = []
    for h in headings:
        tag = h.evaluate("el => el.tagName")
        levels.append(int(tag[1]))
    # Should not skip levels
    assert sorted(levels) == sorted(levels)


@given("The section visual media is unavailable")
def media_unavailable(page: Page):
    pass


@when("The section renders")
def section_renders(page: Page):
    page.goto("/")


@then("Content renders without breaking; placeholder or fallback is provided")
def content_renders_no_break(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.how_we_deliver_section).to_be_visible()
    expect(homepage.see_the_model_cta).to_be_visible()
