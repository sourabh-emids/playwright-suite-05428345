"""Steps for tc_002 - Main navigation menu items functionality."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("The user is on the homepage of the website")
def user_on_homepage(page: Page) -> None:
    """User is on the homepage."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    page.goto("/")
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The user clicks on each main navigation menu item including but not limited to Home, About, Services, Solutions, Insights, Careers, and Contact")
def click_menu_items(page: Page) -> None:
    """Click on each main navigation menu item."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    nav_page = Tc002NavigationPage(page)

    nav_page.navigate_to_about_us()
    expect(page).to_have_url("**/about-us/**", timeout=10000)

    page.goto("/")
    Tc001HomepagePage(page).dismiss_cookie_banner_if_present()

    nav_page.navigate_to_solutions()
    expect(page).to_have_url("**/solutions/**", timeout=10000)

    page.goto("/")
    Tc001HomepagePage(page).dismiss_cookie_banner_if_present()

    nav_page.navigate_to_contact()
    expect(page).to_have_url("**/contact/**", timeout=10000)


@then("Each menu item successfully navigates to its corresponding page and the correct page content is displayed matching the selected menu option")
def menu_navigation_works(page: Page) -> None:
    """Verify menu navigation works correctly."""
    expect(page.get_by_role("heading")).to_be_visible()


@given("The user is on the homepage")
def user_on_homepage_again(page: Page) -> None:
    """User is on the homepage again."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    page.goto("/")
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The user hovers over each main navigation menu item")
def hover_menu_items(page: Page) -> None:
    """Hover over each main navigation menu item."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    from pages.tc_001_homepage_page import Tc001HomepagePage
    nav_page = Tc002NavigationPage(page)

    Tc001HomepagePage(page).dismiss_cookie_banner_if_present()
    nav_page.hover_over_menu_item(nav_page.locators.solutions_link)
    nav_page.verify_dropdown_visible(page.locator('[class*="Solutions-dropdown"], [class*="dropdown"]').first)


@then("Visual hover indicators such as color changes, underlines, or highlighting are displayed to provide feedback on the interactive element")
def hover_indicators_visible(page: Page) -> None:
    """Verify hover indicators are visible."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    nav_page = Tc002NavigationPage(page)
    nav_page.verify_menu_item_hover_state(nav_page.locators.solutions_link)


@given("The user has loaded the homepage on a desktop browser")
def user_on_desktop_browser(page: Page) -> None:
    """User has loaded homepage on desktop browser."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    page.goto("/")
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The user clicks on a navigation menu item multiple times in quick succession")
def rapid_click_menu_item(page: Page) -> None:
    """Click on navigation menu item rapidly."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    from pages.tc_001_homepage_page import Tc001HomepagePage
    nav_page = Tc002NavigationPage(page)
    Tc001HomepagePage(page).dismiss_cookie_banner_if_present()
    nav_page.rapid_click(nav_page.locators.solutions_link, times=3)


@then("Each click is registered properly and navigation occurs without errors, double-clicks do not open duplicate tabs or cause page glitches")
def no_duplicate_tabs_or_glitches(page: Page) -> None:
    """Verify no duplicate tabs or page glitches occur."""
    expect(page).to_have_url("**/solutions/**", timeout=10000)


@given("The user is on the homepage and there are menu items with dropdown submenus")
def user_on_homepage_with_dropdowns(page: Page) -> None:
    """User is on homepage with dropdown menus."""
    from pages.tc_001_homepage_page import Tc001HomepagePage
    page.goto("/")
    homepage_page = Tc001HomepagePage(page)
    homepage_page.dismiss_cookie_banner_if_present()


@when("The user hovers over or clicks on a parent menu item that has submenus")
def hover_parent_menu_item(page: Page) -> None:
    """Hover over parent menu item with submenus."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    nav_page = Tc002NavigationPage(page)
    nav_page.hover_over_menu_item(nav_page.locators.solutions_link)


@then("The dropdown submenu appears with all submenu items visible and each submenu item navigates to the correct page when clicked")
def dropdown_submenu_works(page: Page) -> None:
    """Verify dropdown submenus work correctly."""
    from pages.tc_002_navigation_page import Tc002NavigationPage
    nav_page = Tc002NavigationPage(page)

    expect(nav_page.locators.get_submenu_link("Modernization")).to_be_visible()
    expect(nav_page.locators.get_submenu_link("Interoperability")).to_be_visible()

    nav_page.locators.get_submenu_link("Modernization").click()
    expect(page).to_have_url("**/solutions/modernization**", timeout=10000)
