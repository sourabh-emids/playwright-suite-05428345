"""Steps for tc_004 - Mobile responsive view functionality."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("The user opens the website in a mobile-sized browser window with viewport width of 375px")
def open_mobile_viewport(page: Page) -> None:
    """Open website in mobile viewport."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_mobile_viewport()
    mobile_page.navigate_to_homepage()
    mobile_page.dismiss_cookie_banner()


@when("The homepage loads in mobile view")
def homepage_loads_mobile(page: Page) -> None:
    """Homepage loads in mobile view."""
    page.wait_for_load_state("domcontentloaded")


@then("Text is readable without horizontal scrolling, images scale appropriately, the menu transforms to a mobile menu icon, and all buttons are visible and properly sized for touch interaction")
def verify_mobile_rendering(page: Page) -> None:
    """Verify mobile rendering."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_text_is_readable()
    mobile_page.verify_images_scale()
    mobile_page.verify_no_horizontal_scroll()


@given("The user is on the homepage in mobile view")
def user_on_homepage_mobile(page: Page) -> None:
    """User is on homepage in mobile view."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_mobile_viewport()
    mobile_page.navigate_to_homepage()
    mobile_page.dismiss_cookie_banner()


@when("The user taps on the hamburger menu icon")
def tap_hamburger_menu(page: Page) -> None:
    """Tap the hamburger menu icon."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.click_hamburger_menu()


@then("The mobile navigation menu slides out or expands showing all menu items that can be tapped to navigate to their respective pages")
def verify_mobile_menu_opens(page: Page) -> None:
    """Verify mobile menu opens."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_mobile_menu_opens()


@given("The user has navigated to the contact form on a mobile device")
def user_on_contact_form_mobile(page: Page) -> None:
    """User is on contact form on mobile."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_mobile_viewport()
    mobile_page.navigate_to_contact()
    mobile_page.dismiss_cookie_banner()


@when("The user attempts to fill in form fields and submit")
def fill_and_submit_form(page: Page) -> None:
    """Fill in form fields and submit."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.tap_element(mobile_page.locators.first_name_field)
    page.get_by_label("First Name").fill("Test User")


@then("Form fields are easily tappable, input keyboards open appropriately, and the submit button is prominently visible and functional")
def verify_form_mobile_friendly(page: Page) -> None:
    """Verify form is mobile-friendly."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_buttons_are_tappable()
    expect(page.get_by_label("First Name")).to_be_visible()


@given("The user is viewing the homepage on a mobile device")
def user_viewing_homepage_mobile(page: Page) -> None:
    """User is viewing homepage on mobile device."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_mobile_viewport()
    mobile_page.navigate_to_homepage()
    mobile_page.dismiss_cookie_banner()


@when("The page loads with all hero images and content images")
def page_loads_with_images(page: Page) -> None:
    """Page loads with images."""
    page.wait_for_load_state("networkidle")


@then("Images are optimized for mobile display, do not overflow the screen width, and maintain aspect ratio without distortion")
def verify_images_optimized_mobile(page: Page) -> None:
    """Verify images are optimized for mobile."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_images_scale()
    mobile_page.verify_no_horizontal_scroll()


@given("The user opens the website in a tablet-sized browser window with viewport width of 768px")
def open_tablet_viewport(page: Page) -> None:
    """Open website in tablet viewport."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_tablet_viewport()
    mobile_page.navigate_to_homepage()
    mobile_page.dismiss_cookie_banner()


@when("The homepage loads")
def homepage_loads_tablet(page: Page) -> None:
    """Homepage loads."""
    page.wait_for_load_state("domcontentloaded")


@then("Layout adjusts appropriately for tablet with readable text, visible images, accessible menu, and properly sized buttons without excessive white space or crowding")
def verify_tablet_layout(page: Page) -> None:
    """Verify tablet layout is appropriate."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_text_is_readable()
    mobile_page.verify_images_scale()


@given("The user is on the homepage in mobile view")
def user_on_homepage_mobile_touch(page: Page) -> None:
    """User is on homepage in mobile view for touch tests."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.set_mobile_viewport()
    mobile_page.navigate_to_homepage()
    mobile_page.dismiss_cookie_banner()


@when("The user taps on buttons and links")
def tap_buttons_and_links(page: Page) -> None:
    """Tap buttons and links."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.tap_element(mobile_page.locators.first_name_field)


@then("Touch targets are appropriately sized minimum 44x44 pixels, and no accidental zooming occurs during normal navigation")
def verify_touch_targets_size(page: Page) -> None:
    """Verify touch targets are appropriately sized."""
    from pages.tc_004_mobile_page import Tc004MobilePage
    mobile_page = Tc004MobilePage(page)
    mobile_page.verify_buttons_are_tappable()
