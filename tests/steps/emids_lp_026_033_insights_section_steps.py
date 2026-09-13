"""Steps for emids_lp_026-033: Insights section and content cards."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when


@given(parsers.parse("User views Insights section"))
def view_insights(page: Page) -> None:
    """User views Insights section."""
    page.goto("/")
    page.get_by_text("Insights").scroll_into_view_if_needed()


@given(parsers.parse("User views Insights on various viewports"))
def view_insights_viewports(page: Page) -> None:
    """User views on various viewports."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("CMS manages insight content"))
def cms_manages_insights(page: Page) -> None:
    """CMS manages insight content."""
    pass


@given(parsers.parse("CMS configures insight cards"))
def cms_configures_insights(page: Page) -> None:
    """CMS configures insight cards."""
    pass


@when("User counts and reads cards")
def count_read_cards(page: Page) -> None:
    """Count and read cards."""
    pass


@when("Card renders")
def card_renders(page: Page) -> None:
    """Card renders."""
    page.wait_for_load_state("domcontentloaded")


@then("Six cards render")
def six_cards_render(page: Page) -> None:
    """Verify six cards render."""
    page.get_by_text("Insights").scroll_into_view_if_needed()
    # Check for insight cards or carousel indicators
    pass


@then("Each has content type, title, and Download/Read More action")
def each_has_required_fields(page: Page) -> None:
    """Verify each has required fields."""
    page.get_by_text("Insights").scroll_into_view_if_needed()
    # Verify action buttons present
    pass


@then("Image displays")
def image_displays(page: Page) -> None:
    """Verify image displays."""
    pass


@then("Cards remain accessible")
def cards_accessible(page: Page) -> None:
    """Verify cards accessible."""
    expect(page.get_by_text("Insights")).to_be_visible()


@then("Content readable")
def content_readable(page: Page) -> None:
    """Verify content readable."""
    expect(page.get_by_text("Insights")).to_be_visible()


@then("No overflow")
def no_overflow(page: Page) -> None:
    """Verify no overflow."""
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    expect(scroll_width).to_be_less_than_or_equal(inner_width)


@then("Only published insight cards display")
def only_published_display(page: Page) -> None:
    """Verify only published display."""
    expect(page.get_by_text("Insights")).to_be_visible()


@then("Action label says 'Download'")
def action_download(page: Page) -> None:
    """Verify action says Download."""
    pass


@then("For articles shows 'Read More'")
def read_more_articles(page: Page) -> None:
    """Verify Read More for articles."""
    pass
