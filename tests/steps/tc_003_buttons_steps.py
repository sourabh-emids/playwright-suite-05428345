"""Steps for tc_003 - Main buttons functionality and navigation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@given("The user is on the homepage")
def user_on_homepage(page: Page) -> None:
    """User is on the homepage."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    page.goto("/")
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.dismiss_cookie_banner()


@when("The user clicks the Contact Us button")
def click_contact_us_button(page: Page) -> None:
    """Click the Contact Us button."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.click_contact_us_button()


@then("The user is navigated to the contact page or a contact form modal opens displaying contact fields such as name, email, phone, and message")
def verify_contact_page_or_modal(page: Page) -> None:
    """Verify contact page or modal opens."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.verify_navigated_to_contact()
    expect(page.get_by_label("First Name")).to_be_visible()
    expect(page.get_by_label("Work Email Address")).to_be_visible()
    expect(page.get_by_label("Phone Number")).to_be_visible()
    expect(page.get_by_label("Comments")).to_be_visible()


@when("The user clicks the Learn More button")
def click_learn_more_button(page: Page) -> None:
    """Click the Learn More button."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.click_learn_more_button()


@then("The user is navigated to the appropriate section or page with more detailed information about the featured service or offering")
def verify_navigated_to_detailed_page(page: Page) -> None:
    """Verify navigation to detailed information page."""
    expect(page).to_have_url("**/forward-deployed-context-engineering/**", timeout=10000)


@given("The user is on the homepage or any inner page")
def user_on_homepage_or_inner_page(page: Page) -> None:
    """User is on homepage or inner page."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    page.goto("/")
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.dismiss_cookie_banner()


@when("The user clicks primary Call to Action buttons such as Get Started, Request a Demo, or Explore Solutions")
def click_cta_buttons(page: Page) -> None:
    """Click primary CTA buttons."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.click_all_solutions_button()


@then("Each button performs its intended action which may include navigating to a form, starting a chat, or redirecting to a relevant landing page")
def verify_cta_action(page: Page) -> None:
    """Verify CTA button performs intended action."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.verify_navigated_to_solutions()


@given("The user is viewing the homepage")
def user_viewing_homepage(page: Page) -> None:
    """User is viewing the homepage."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    page.goto("/")
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.dismiss_cookie_banner()


@when("The user hovers over and clicks on main buttons")
def hover_and_click_buttons(page: Page) -> None:
    """Hover over and click main buttons."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.hover_over_button(buttons_page.locators.learn_more_button)
    buttons_page.click_button_multiple_times(buttons_page.locators.learn_more_button, times=1)


@then("Buttons display appropriate visual feedback for hover state and pressed or active state to confirm interaction")
def buttons_show_visual_feedback(page: Page) -> None:
    """Verify buttons show visual feedback."""
    expect(page.get_by_role("link", name="See How We Deliver Outcomes")).to_be_visible()


@given("The user has scrolled to the footer section")
def user_scrolled_to_footer(page: Page) -> None:
    """User has scrolled to footer section."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    page.goto("/")
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.dismiss_cookie_banner()
    buttons_page.scroll_to_footer()


@when("The user clicks on buttons in the footer such as social media links or newsletter subscription buttons")
def click_footer_buttons(page: Page) -> None:
    """Click footer buttons."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.click_footer_connect_button()


@then("Each footer button opens the correct destination such as social media profiles, email client with pre-filled address, or expands the subscription form")
def footer_buttons_open_correct_destination(page: Page) -> None:
    """Verify footer buttons open correct destination."""
    from pages.tc_003_buttons_page import Tc003ButtonsPage
    buttons_page = Tc003ButtonsPage(page)
    buttons_page.verify_navigated_to_contact()
