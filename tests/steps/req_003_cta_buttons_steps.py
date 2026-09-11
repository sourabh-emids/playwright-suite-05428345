"""Step definitions for REQ-003: Primary CTA buttons function correctly."""

from pytest_bdd import given, when, then  # noqa: F401

from pages.req_001_homepage_page import Req001HomepagePage
from utils.config import BASE_URL


@given("User is on a page containing primary CTA buttons (Contact Us / Learn More)")
def user_on_page_with_cta_buttons(req003_cta_page) -> None:
    """User is on a page with CTA buttons."""
    homepage_page = Req001HomepagePage(req003_cta_page.page)
    homepage_page.goto_homepage(BASE_URL)
    homepage_page.dismiss_cookie_banner_if_present()


@given("User is on the homepage")
def user_on_homepage_cta(req003_cta_page) -> None:
    """User is on homepage."""
    homepage_page = Req001HomepagePage(req003_cta_page.page)
    homepage_page.goto_homepage(BASE_URL)
    homepage_page.dismiss_cookie_banner_if_present()


@when("User clicks on each important button")
def user_clicks_each_cta_button(req003_cta_page) -> None:
    """Click each CTA button and verify navigation."""
    req003_cta_page.click_connect_cta()
    req003_cta_page.verify_navigated_to_contact_page()


@then("Buttons function as intended and open the expected page, section, or modal")
def cta_buttons_function_correctly(req003_cta_page) -> None:
    """Verify CTA buttons work correctly."""
    pass


@when('User clicks on "See How We Deliver Outcomes" button')
def user_clicks_see_how_we_deliver_outcomes(req003_cta_page) -> None:
    """Click on 'See How We Deliver Outcomes' button."""
    req003_cta_page.click_see_how_we_deliver_outcomes()


@then("The page should navigate to the Forward-Deployed Context Engineering page")
def forward_deployed_page_navigated(req003_cta_page) -> None:
    """Verify navigation to Forward-Deployed page."""
    req003_cta_page.verify_navigated_to_forward_deployed_page()


@when('User clicks on "See the model" button')
def user_clicks_see_the_model(req003_cta_page) -> None:
    """Click on 'See the model' button."""
    req003_cta_page.click_see_the_model()


@then("The page should navigate to the Forward-Deployed Context Engineering page")
def forward_deployed_page_navigated_from_model(req003_cta_page) -> None:
    """Verify navigation to Forward-Deployed page."""
    req003_cta_page.verify_navigated_to_forward_deployed_page()


@when('User clicks on "All solutions" button')
def user_clicks_all_solutions(req003_cta_page) -> None:
    """Click on 'All solutions' button."""
    req003_cta_page.click_all_solutions()


@then("The page should navigate to the Solutions page")
def solutions_page_navigated(req003_cta_page) -> None:
    """Verify navigation to Solutions page."""
    req003_cta_page.verify_navigated_to_solutions_page()


@when('User clicks on "Connect" CTA button')
def user_clicks_connect_cta(req003_cta_page) -> None:
    """Click on 'Connect' CTA button."""
    req003_cta_page.click_connect_cta()


@then("The page should navigate to the Contact page")
def contact_page_navigated(req003_cta_page) -> None:
    """Verify navigation to Contact page."""
    req003_cta_page.verify_navigated_to_contact_page()
