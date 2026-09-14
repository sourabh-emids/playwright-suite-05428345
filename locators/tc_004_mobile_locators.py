"""Locators for tc_004 - Mobile responsive view functionality."""
from playwright.sync_api import Locator, Page


class Tc004MobileLocators:
    """Locators for mobile responsive functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def hamburger_menu(self) -> Locator:
        """Hamburger menu icon for mobile."""
        return self.page.locator('[aria-label="Menu"], [class*="menu"], button[class*="menu"], [class*="hamburger"]').first

    @property
    def mobile_navigation(self) -> Locator:
        """Mobile navigation menu."""
        return self.page.locator('[class*="mobile-menu"], [class*="nav-menu"], [role="navigation"]').first

    @property
    def contact_form(self) -> Locator:
        """Contact form on contact page."""
        return self.page.locator('form, [class*="contact-form"]').first

    @property
    def first_name_field(self) -> Locator:
        """First name field in contact form."""
        return self.page.get_by_label("First Name")

    @property
    def submit_button(self) -> Locator:
        """Submit button."""
        return self.page.get_by_role("button", name="Submit")

    @property
    def hero_image(self) -> Locator:
        """Hero image on homepage."""
        return self.page.locator('[class*="hero"], [class*="banner"] img').first

    @property
    def all_images(self) -> Locator:
        """All images on the page."""
        return self.page.locator("img")

    @property
    def navigation_items(self) -> Locator:
        """Navigation menu items."""
        return self.page.locator('[class*="menu"] li, nav li').first

    @property
    def text_content(self) -> Locator:
        """Text content on the page."""
        return self.page.locator("main p, main h1, main h2, main h3").first
