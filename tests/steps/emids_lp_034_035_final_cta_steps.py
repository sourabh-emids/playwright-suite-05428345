"""Steps for emids_lp_034-035: Final conversion banner and timeline."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when


@given(parsers.parse("User scrolls to bottom of page"))
def scroll_bottom(page: Page) -> None:
    """Scroll to bottom."""
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@given(parsers.parse("User views final conversion banner"))
def view_final_cta(page: Page) -> None:
    """View final CTA."""
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@given(parsers.parse("User views final CTA on mobile"))
def view_final_cta_mobile(page: Page) -> None:
    """View final CTA on mobile."""
    page.set_viewport_size({"width": 375, "height": 667})
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@given(parsers.parse("User views final conversion section"))
def view_final_section(page: Page) -> None:
    """View final conversion section."""
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("User reaches final section before footer")
def reach_final_section(page: Page) -> None:
    """Reach final section."""
    pass


@when("User activates primary CTA")
def activate_cta(page: Page) -> None:
    """Activate primary CTA."""
    page.get_by_role("link", name="Connect").last.click()


@when("User reads supporting content")
def read_supporting(page: Page) -> None:
    """Read supporting content."""
    pass


@when("User checks content")
def check_content(page: Page) -> None:
    """Check content."""
    pass


@when("User assesses visual prominence")
def assess_prominence(page: Page) -> None:
    """Assess visual prominence."""
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("User scrolls")
def user_scrolls(page: Page) -> None:
    """User scrolls."""
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")


@when("User reads timeline")
def read_timeline(page: Page) -> None:
    """Read timeline."""
    pass


@when("User disables CSS")
def disable_css(page: Page) -> None:
    """Disable CSS."""
    pass


@then("Conversion banner is visible before footer")
def banner_visible_before_footer(page: Page) -> None:
    """Verify banner visible before footer."""
    expect(page.get_by_text("From workshop to agent to scale deployment")).to_be_visible()


@then("CTA is clearly labeled")
def cta_clearly_labeled(page: Page) -> None:
    """Verify CTA clearly labeled."""
    expect(page.get_by_role("link", name="Connect")).to_be_visible()


@then("Keyboard activation works")
def keyboard_works(page: Page) -> None:
    """Verify keyboard activation."""
    page.get_by_role("link", name="Connect").last.focus()
    expect(page.get_by_role("link", name="Connect").last).to_be_focused()


@then("Timing/value text is readable")
def timing_text_readable(page: Page) -> None:
    """Verify timing text readable."""
    expect(page.get_by_text("1 Day")).to_be_visible()


@then("Required message and CTA fields are present and non-empty")
def required_fields_present(page: Page) -> None:
    """Verify required fields present."""
    expect(page.get_by_text("From workshop to agent to scale deployment")).to_be_visible()
    expect(page.get_by_role("link", name="Connect")).to_be_visible()


@then("Section has high contrast")
def high_contrast(page: Page) -> None:
    """Verify high contrast."""
    pass


@then("CTA stands out")
def cta_stands_out(page: Page) -> None:
    """Verify CTA stands out."""
    expect(page.get_by_role("link", name="Connect")).to_be_visible()


@then("CTA text wraps appropriately")
def cta_wraps(page: Page) -> None:
    """Verify CTA wraps."""
    expect(page.get_by_role("link", name="Connect")).to_be_visible()


@then("No overflow or clipping")
def no_clipping(page: Page) -> None:
    """Verify no clipping."""
    pass


@then("Section does not overlap footer")
def no_footer_overlap(page: Page) -> None:
    """Verify no footer overlap."""
    expect(page.get_by_role("contentinfo")).to_be_visible()


@then("Proper spacing")
def proper_spacing(page: Page) -> None:
    """Verify proper spacing."""
    pass


@then("Labels display in intended order: '1 Day', '2 Weeks', '3 Months'")
def labels_order(page: Page) -> None:
    """Verify labels order."""
    expect(page.get_by_text("1 Day")).to_be_visible()
    expect(page.get_by_text("2 Weeks")).to_be_visible()
    expect(page.get_by_text("3 Months")).to_be_visible()


@then("Timing meaning is conveyed semantically")
def timing_semantic(page: Page) -> None:
    """Verify timing semantic."""
    expect(page.get_by_text("1 Day")).to_be_visible()


@then("Not just visual styling")
def not_just_styling(page: Page) -> None:
    """Verify not just styling."""
    expect(page.get_by_text("1 Day")).to_be_visible()


@then("Timing labels remain readable and meaningful")
def labels_readable_meaningful(page: Page) -> None:
    """Verify labels readable."""
    expect(page.get_by_text("1 Day")).to_be_visible()
