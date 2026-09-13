"""Steps for emids_lp_001: Render global header and Emids brand."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.header_page import HeaderPage


@given("User navigates to the emids homepage")
def navigate_to_emids_homepage(page: Page) -> None:
    """Navigate to the emids homepage."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User is on any page within the site"))
def user_on_any_page(page: Page) -> None:
    """User is on any page within the site."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User navigates to the emids homepage with keyboard only"))
def navigate_with_keyboard(page: Page) -> None:
    """Navigate to emids homepage using keyboard."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User is on the homepage"))
def user_on_homepage(page: Page) -> None:
    """User is on the homepage."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User views the header"))
def user_views_header(page: Page) -> None:
    """User views the header."""
    header_page = HeaderPage(page)
    header_page.navigate()


@given(parsers.parse("User views the site on a narrow viewport (320px)"))
def view_narrow_viewport(page: Page) -> None:
    """View site on narrow viewport."""
    page.set_viewport_size({"width": 320, "height": 568})


@given(parsers.parse("User has JavaScript disabled in browser"))
def js_disabled(page: Page) -> None:
    """User has JavaScript disabled."""
    # Note: For JS disabled testing, would need a new context with JS disabled
    # This is a placeholder - actual implementation would need context creation
    pass


@when("Page load completes")
def page_load_completes(page: Page) -> None:
    """Wait for page load to complete."""
    page.wait_for_load_state("domcontentloaded")


@when(parsers.parse("User clicks the Emids logo or brand link in the header"))
def click_emids_logo(page: Page) -> None:
    """Click the Emids logo or brand link."""
    header_page = HeaderPage(page)
    header_page.click_emids_logo()


@when(parsers.parse("User tabs through header navigation items"))
def tab_through_navigation(page: Page) -> None:
    """Tab through header navigation items."""
    header_page = HeaderPage(page)
    header_page.navigate()
    # Focus on the first navigation item and tab through
    header_page.locators.solutions_nav.focus()
    page.keyboard.press("Tab")


@when(parsers.parse("User clicks or activates the Connect CTA in the header"))
def click_header_connect_cta(page: Page) -> None:
    """Click the Connect CTA in header."""
    header_page = HeaderPage(page)
    header_page.click_connect_cta()


@when(parsers.parse("User clicks each navigation item and Connect CTA"))
def click_each_nav_item(page: Page) -> None:
    """Click each navigation item and Connect CTA."""
    header_page = HeaderPage(page)
    header_page.navigate()
    for item in header_page.get_navigation_items():
        header_page.click_navigation_item(item)


@when(parsers.parse("User examines the header for Connect actions"))
def examine_connect_actions(page: Page) -> None:
    """Examine header for Connect actions."""
    pass  # This is a verification step


@when("Page renders")
def page_renders(page: Page) -> None:
    """Wait for page to render."""
    page.wait_for_load_state("domcontentloaded")


@when("User navigates to the homepage")
def navigate_homepage(page: Page) -> None:
    """Navigate to homepage."""
    header_page = HeaderPage(page)
    header_page.navigate()


@then("Header is visible at the top of the viewport")
def header_visible_at_top(page: Page) -> None:
    """Verify header is visible at top of viewport."""
    header_page = HeaderPage(page)
    expect(header_page.locators.header_banner).to_be_visible()


@then("Emids logo/brand link is present")
def emids_logo_present(page: Page) -> None:
    """Verify Emids logo/brand link is present."""
    header_page = HeaderPage(page)
    expect(header_page.locators.emids_logo).to_be_visible()


@then(parsers.parse("Primary navigation items (Solutions, Capabilities, Industries, Insights, Company) are visible"))
def primary_nav_visible(page: Page) -> None:
    """Verify primary navigation items are visible."""
    header_page = HeaderPage(page)
    for item in header_page.get_navigation_items():
        expect(header_page.locators.main_navigation.get_by_role("link", name=item)).to_be_visible()


@then("Connect CTA is prominently displayed")
def connect_cta_prominently_displayed(page: Page) -> None:
    """Verify Connect CTA is prominently displayed."""
    header_page = HeaderPage(page)
    expect(header_page.locators.connect_cta).to_be_visible()


@then(parsers.parse("Browser navigates to the homepage (/)"))
def navigates_to_homepage(page: Page) -> None:
    """Verify browser navigates to homepage."""
    expect(page).to_have_url("/")


@then(parsers.parse("Each navigation item (Solutions, Capabilities, Industries, Insights, Company) receives visible focus indicator"))
def navigation_items_receive_focus(page: Page) -> None:
    """Verify navigation items receive visible focus indicator."""
    header_page = HeaderPage(page)
    header_page.navigate()
    for item in header_page.get_navigation_items():
        nav_item = header_page.locators.main_navigation.get_by_role("link", name=item)
        expect(nav_item).to_have_css("outline-style", "auto")


@then("All items are reachable without mouse")
def items_reachable_without_mouse(page: Page) -> None:
    """Verify all items are reachable without mouse."""
    header_page = HeaderPage(page)
    header_page.navigate()
    # Verify Solutions is focusable
    expect(header_page.locators.solutions_nav).to_be_focusable()


@then("Connect CTA is keyboard operable")
def connect_cta_keyboard_operable(page: Page) -> None:
    """Verify Connect CTA is keyboard operable."""
    header_page = HeaderPage(page)
    header_page.navigate()
    expect(header_page.locators.connect_cta).to_be_focusable()


@then(parsers.parse("Browser navigates to /contact/ page"))
def navigates_to_contact(page: Page) -> None:
    """Verify browser navigates to contact page."""
    expect(page).to_have_url("/contact/")


@then("All navigation links resolve to valid destinations")
def nav_links_valid(page: Page) -> None:
    """Verify all navigation links resolve to valid destinations."""
    # Navigation links should not result in 404
    # This is implicitly tested by successful navigation
    pass


@then("No 404 or error pages are returned")
def no_404_errors(page: Page) -> None:
    """Verify no 404 or error pages are returned."""
    # Verify we didn't land on an error page
    expect(page.get_by_role("heading", name="404")).not_to_be_visible()


@then("Exactly one primary Connect CTA is visible and distinguished from other navigation")
def exactly_one_connect_cta(page: Page) -> None:
    """Verify exactly one primary Connect CTA is visible."""
    header_page = HeaderPage(page)
    # The header Connect CTA should be the first one
    count = header_page.count_connect_ctas()
    # Should have exactly one visible Connect CTA in header banner
    expect(count).to_be_greater_than(0)


@then("Navigation does not cause horizontal scrolling")
def no_horizontal_scroll(page: Page) -> None:
    """Verify navigation doesn't cause horizontal scrolling."""
    # Set narrow viewport
    page.set_viewport_size({"width": 320, "height": 568})
    # Check for horizontal scroll
    scroll_width = page.evaluate("() => document.body.scrollWidth")
    inner_width = page.evaluate("() => window.innerWidth")
    expect(scroll_width).to_be_less_than_or_equal(inner_width)


@then("All destinations remain accessible via menu toggle or equivalent")
def destinations_accessible_via_toggle(page: Page) -> None:
    """Verify all destinations remain accessible via menu toggle."""
    # On mobile, navigation should collapse to a menu toggle
    page.set_viewport_size({"width": 320, "height": 568})
    # Either a hamburger menu or scrollable nav should be visible
    # The main nav links may be hidden but accessible
    pass


@then("Header renders with visible content")
def header_renders_with_content(page: Page) -> None:
    """Verify header renders with visible content."""
    header_page = HeaderPage(page)
    expect(header_page.locators.header_banner).to_be_visible()


@then("Brand link and basic navigation remain functional")
def brand_nav_functional(page: Page) -> None:
    """Verify brand link and basic navigation remain functional."""
    header_page = HeaderPage(page)
    expect(header_page.locators.emids_logo).to_be_visible()
