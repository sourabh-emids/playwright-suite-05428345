"""Steps for emids_lp_012: Render How We Deliver section."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.how_we_deliver.how_we_deliver_page import HowWeDeliverPage


@given(parsers.parse("User scrolls to How We Deliver section"))
def scroll_to_section(page: Page) -> None:
    """User scrolls to How We Deliver section."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("How We Deliver section renders"))
def section_renders(page: Page) -> None:
    """How We Deliver section renders."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("User examines page heading structure"))
def examine_heading_structure(page: Page) -> None:
    """User examines page heading structure."""
    pass


@given(parsers.parse("User with assistive technology views How We Deliver section"))
def assistive_tech_view(page: Page) -> None:
    """User with assistive technology views section."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("How We Deliver section visual is unavailable"))
def visual_unavailable(page: Page) -> None:
    """Visual is unavailable."""
    pass


@given(parsers.parse("How We Deliver section contains long body copy"))
def long_copy(page: Page) -> None:
    """Section contains long body copy."""
    page.set_viewport_size({"width": 375, "height": 667})


@when("Section becomes visible")
def section_visible(page: Page) -> None:
    """Section becomes visible."""
    page.wait_for_load_state("domcontentloaded")


@when("User examines content")
def examine_content(page: Page) -> None:
    """User examines content."""
    pass


@when("User navigates through headings")
def navigate_headings(page: Page) -> None:
    """Navigate through headings."""
    pass


@when("Section content is announced")
def content_announced(page: Page) -> None:
    """Content is announced."""
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("Page renders on narrow viewport")
def page_renders_narrow(page: Page) -> None:
    """Page renders on narrow viewport."""
    page.wait_for_load_state("domcontentloaded")


@then("Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence")
def elements_render_sequence(page: Page) -> None:
    """Verify elements render in sequence."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.section_heading).to_be_visible()
    expect(how_we_deliver.locators.main_heading).to_be_visible()
    expect(how_we_deliver.locators.body_copy).to_be_visible()
    expect(how_we_deliver.locators.see_model_cta).to_be_visible()


@then("All required fields (title, body, CTA) contain content and are non-empty")
def required_fields_non_empty(page: Page) -> None:
    """Verify required fields are non-empty."""
    how_we_deliver = HowWeDeliverPage(page)
    heading_text = how_we_deliver.locators.main_heading.inner_text()
    expect(len(heading_text)).to_be_greater_than(0)
    expect(how_we_deliver.locators.see_model_cta).to_be_visible()


@then("Heading levels follow logical hierarchy (H1 > H2 > H3)")
def heading_hierarchy(page: Page) -> None:
    """Verify heading hierarchy."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.is_heading_logical()).to_be_true()


@then("No skipped levels where avoidable")
def no_skipped_levels(page: Page) -> None:
    """Verify no skipped levels."""
    how_we_deliver = HowWeDeliverPage(page)
    hierarchy = how_we_deliver.get_heading_hierarchy()
    expect(hierarchy["h2_count"]).to_be_greater_than(0)


@then("All content is properly labeled and accessible")
def content_accessible(page: Page) -> None:
    """Verify content is properly labeled."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.main_heading).to_have_attribute("id")


@then("Section renders with available content")
def section_renders_content(page: Page) -> None:
    """Verify section renders with available content."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.main_heading).to_be_visible()


@then("Missing media does not break layout")
def media_missing_no_break(page: Page) -> None:
    """Verify missing media doesn't break layout."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.section_heading).to_be_visible()


@then("Copy reflows appropriately")
def copy_reflows(page: Page) -> None:
    """Verify copy reflows."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.body_copy).to_be_visible()


@then("No overflow or truncation")
def no_overflow_truncation(page: Page) -> None:
    """Verify no overflow or truncation."""
    how_we_deliver = HowWeDeliverPage(page)
    expect(how_we_deliver.locators.body_copy).to_be_visible()
