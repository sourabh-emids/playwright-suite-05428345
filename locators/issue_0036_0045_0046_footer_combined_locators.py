"""Locators for issue_0036, 0045-0046: Footer combined"""

from playwright.sync_api import Page, Locator


class FooterLocators:
    """Locators for Footer section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        """Returns the footer element."""
        return self.page.locator("footer").first

    @property
    def cookie_preferences(self) -> Locator:
        """Returns the Cookie Preferences button."""
        return self.page.get_by_text("Cookie Preferences").first

    @property
    def privacy_policy_link(self) -> Locator:
        """Returns the Privacy Policy link."""
        return self.page.get_by_role("link", name="Privacy Policy").first

    @property
    def social_links(self) -> Locator:
        """Returns social links."""
        return self.page.locator("footer a[href*='linkedin'], footer a[href*='twitter']")
