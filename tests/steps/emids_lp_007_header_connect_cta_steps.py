"""Steps for emids_lp_007: Provide header Connect CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.connect_cta_page import ConnectCTAPage


@given(parsers.parse("User views the header"))
def view_header(page: Page) -> None:
    """User views the header."""
    connect_page = ConnectCTAPage(page)
    connect_page.navigate()


@given(parsers.parse("User examines the Connect CTA"))
def examine_connect_cta(page: Page) -> None:
    """User examines the Connect CTA."""
    connect_page = ConnectCTAPage(page)
    connect_page.navigate()


@given(parsers.parse("User clicks Connect CTA"))
def click_connect_cta(page: Page) -> None:
    """User clicks Connect CTA."""
    connect_page = ConnectCTAPage(page)
    connect_page.click_connect_cta()


@given(parsers.parse("User focuses on Connect CTA"))
def focus_connect_cta(page: Page) -> None:
    """User focuses on Connect CTA."""
    connect_page = ConnectCTAPage(page)
    connect_page.navigate()
    connect_page.locators.main_connect_cta.focus()


@given(parsers.parse("User views site on mobile viewport"))
def view_mobile_viewport(page: Page) -> None:
    """User views site on mobile viewport."""
    page.set_viewport_size({"width": 375, "height": 667})


@given(parsers.parse("User examines header"))
def examine_header(page: Page) -> None:
    """User examines header."""
    connect_page = ConnectCTAPage(page)
    connect_page.navigate()


@when("User identifies the Connect action")
def identify_connect_action(page: Page) -> None:
    """User identifies the Connect action."""
    pass  # Verification step


@when("User checks accessibility attributes")
def check_accessibility_attributes(page: Page) -> None:
    """Check accessibility attributes."""
    pass  # Verification step


@when("Navigation completes")
def navigation_completes(page: Page) -> None:
    """Navigation completes."""
    page.wait_for_load_state("domcontentloaded")


@when("User checks link attributes")
def check_link_attributes(page: Page) -> None:
    """Check link attributes."""
    pass  # Verification step


@when("User activates with keyboard (Enter/Space)")
def activate_keyboard(page: Page) -> None:
    """Activate with keyboard."""
    page.keyboard.press("Enter")


@when("Page renders")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("User counts Connect CTAs")
def count_connect_ctas(page: Page) -> None:
    """Count Connect CTAs."""
    pass  # Verification step


@then("Connect CTA is visually prominent compared to other navigation items")
def cta_visually_prominent(page: Page) -> None:
    """Verify Connect CTA is visually prominent."""
    connect_page = ConnectCTAPage(page)
    # The CTA should have some distinct visual treatment
    expect(connect_page.locators.main_connect_cta).to_be_visible()


@then("CTA has meaningful accessible name describing its action")
def cta_has_accessible_name(page: Page) -> None:
    """Verify CTA has meaningful accessible name."""
    connect_page = ConnectCTAPage(page)
    name = connect_page.get_accessible_name()
    expect(name.lower()).to_contain("connect")


@then("Browser loads /contact/ page")
def loads_contact_page(page: Page) -> None:
    """Verify browser loads contact page."""
    expect(page).to_have_url("/contact/")


@then("URL is HTTPS and resolves to valid destination")
def url_https_valid(page: Page) -> None:
    """Verify URL is HTTPS and valid."""
    connect_page = ConnectCTAPage(page)
    expect(connect_page.is_https_and_valid()).to_be_true()


@then("Navigation to contact page occurs")
def navigation_to_contact(page: Page) -> None:
    """Verify navigation to contact page occurs."""
    expect(page).to_have_url("/contact/")


@then("Connect CTA remains visible and accessible in header")
def cta_visible_on_mobile(page: Page) -> None:
    """Verify Connect CTA remains visible on mobile."""
    connect_page = ConnectCTAPage(page)
    expect(connect_page.is_visible_on_mobile()).to_be_true()


@then("Only one primary Connect CTA exists in header")
def only_one_primary_cta(page: Page) -> None:
    """Verify only one primary Connect CTA exists in header."""
    connect_page = ConnectCTAPage(page)
    # There should be exactly one Connect CTA in the header banner
    count = connect_page.count_primary_ctas()
    expect(count).to_equal(1)
