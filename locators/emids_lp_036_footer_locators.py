"""Locators for emids_lp_036, emids_lp_045-046: Footer."""
from playwright.sync_api import Locator, Page


class EmidsLp036FooterLocators:
    """Locators for footer verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def cookie_preferences_button(self) -> Locator:
        return self.page.locator('button:has-text("Cookie Preferences"), a:has-text("Cookie Preferences")').first

    @property
    def privacy_link(self) -> Locator:
        return self.page.locator('a:has-text("Privacy Policy"), footer a[href*="privacy"]').first

    @property
    def cookie_policy_link(self) -> Locator:
        return self.page.locator('a:has-text("Cookie Policy"), footer a[href*="cookie"]').first

    @property
    def accessibility_link(self) -> Locator:
        return self.page.locator('a:has-text("Accessibility"), footer a[href*="accessibility"]').first

    @property
    def social_links(self) -> Locator:
        return self.footer.locator('a[href*="linkedin"], a[href*="twitter"], a[href*="youtube"]')
