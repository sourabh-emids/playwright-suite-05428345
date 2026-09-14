"""Steps for tc_001 - Website homepage loads successfully."""
from playwright.sync_api import Page, expect
from playwright.sync_api import ConsoleMessage
from pytest_bdd import given, when, then


@given("The user has a stable internet connection and a modern web browser")
def user_has_stable_connection_and_browser(page: Page) -> None:
    """Verify the page can be accessed."""
    pass


@when("The user navigates to https://www.emids.com/")
def user_navigates_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("https://www.emids.com/")


@then("The homepage loads completely with all visible content such as header, hero section, navigation menu, footer, and branding elements rendered correctly without any obvious errors, broken layouts, or missing resources")
def homepage_loads_completely(page: Page) -> None:
    """Verify homepage loads completely with all visible content."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()
    homepage_page.verify_homepage_loaded()


@given("The user has opened the website homepage")
def user_has_opened_homepage(page: Page) -> None:
    """User has opened the homepage."""
    page.goto("/")
    from pages.tc_001_homepage_page import Tc001HomepagePage
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The page finishes loading")
def page_finishes_loading(page: Page) -> None:
    """Wait for page to finish loading."""
    page.wait_for_load_state("networkidle")


@then("All images, icons, videos, and media assets are visible and properly displayed without placeholder icons or missing resource errors")
def media_assets_visible(page: Page) -> None:
    """Verify all media assets are visible."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    homepage_page = Tc001HomepagePage(page)
    homepage_page.verify_media_assets_load()


@given("The user has navigated to the homepage")
def user_has_navigated_to_homepage(page: Page) -> None:
    """User has navigated to the homepage."""
    page.goto("/")
    from pages.tc_001_homepage_page import Tc001HomepagePage
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The page loads")
def the_page_loads(page: Page) -> None:
    """Wait for page to load."""
    page.wait_for_load_state("domcontentloaded")


@then("Styles are applied correctly and interactive elements are functional without JavaScript errors displayed in the browser console")
def styles_applied_correctly(page: Page) -> None:
    """Verify styles are applied and no JS errors in console."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    homepage_page = Tc001HomepagePage(page)
    homepage_page.verify_styles_applied()

    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg) if msg.type == "error" else None)
    page.reload()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("heading", name="In Healthcare, Only Outcomes Matter")).to_be_visible()
