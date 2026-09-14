"""Page object for tc_003 - Main buttons functionality and navigation."""
from playwright.sync_api import Page, expect, Locator

from locators.tc_003_buttons_locators import Tc003ButtonsLocators


class Tc003ButtonsPage:
    """Page object for buttons functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Tc003ButtonsLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def dismiss_cookie_banner(self) -> None:
        """Dismiss the cookie consent banner."""
        if self.locators.cookie_allow_button.is_visible():
            self.locators.cookie_allow_button.click()

    def click_contact_us_button(self) -> None:
        """Click the Contact Us button."""
        self.locators.contact_us_button.click()

    def click_learn_more_button(self) -> None:
        """Click the Learn More button."""
        self.locators.learn_more_button.click()

    def click_all_solutions_button(self) -> None:
        """Click the All Solutions button."""
        self.locators.all_solutions_button.click()

    def click_footer_connect_button(self) -> None:
        """Click the footer Connect button."""
        self.locators.footer_connect_button.click()

    def click_cta_button(self, button: Locator) -> None:
        """Click a CTA button."""
        button.click()

    def verify_navigated_to_contact(self) -> None:
        """Verify navigation to contact page."""
        expect(self.page).to_have_url("**/contact/**", timeout=10000)

    def verify_navigated_to_solutions(self) -> None:
        """Verify navigation to solutions page."""
        expect(self.page).to_have_url("**/solutions/**", timeout=10000)

    def scroll_to_footer(self) -> None:
        """Scroll to footer section."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def hover_over_button(self, button: Locator) -> None:
        """Hover over a button."""
        button.hover()

    def click_button_multiple_times(self, button: Locator, times: int = 3) -> None:
        """Click a button multiple times."""
        for _ in range(times):
            button.click()
