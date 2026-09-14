"""Locators for tc_003 - Main buttons functionality and navigation."""
from playwright.sync_api import Locator, Page


class Tc003ButtonsLocators:
    """Locators for buttons functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def contact_us_button(self) -> Locator:
        """Button to navigate to contact page."""
        return self.page.get_by_role("link", name="Connect").first

    @property
    def learn_more_button(self) -> Locator:
        """Learn More button."""
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def all_solutions_button(self) -> Locator:
        """All solutions button."""
        return self.page.get_by_role("link", name="All solutions")

    @property
    def footer_connect_button(self) -> Locator:
        """Connect button in footer."""
        return self.page.locator("contentinfo").get_by_role("link", name="Connect")

    @property
    def primary_cta_buttons(self) -> Locator:
        """Primary CTA buttons."""
        return self.page.get_by_role("link", name="Connect")

    @property
    def submit_button(self) -> Locator:
        """Submit button."""
        return self.page.get_by_role("button", name="Submit")

    @property
    def cookie_allow_button(self) -> Locator:
        """Allow cookies button."""
        return self.page.get_by_role("button", name="Allow all")

    def get_button_by_text(self, text: str) -> Locator:
        """Get a button by its text."""
        return self.page.get_by_role("button", name=text)

    def get_link_by_text(self, text: str) -> Locator:
        """Get a link by its text."""
        return self.page.get_by_role("link", name=text)
