"""Locators for Cookie Preferences control exposure (issue_0036)."""
from playwright.sync_api import Locator, Page


class CookiePreferencesLocators:
    """Locators for Cookie Preferences elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer")

    @property
    def cookie_preferences(self) -> Locator:
        return self.page.get_by_role("button", name=re.compile("Cookie", re.IGNORECASE)).or_(
            self.page.get_by_role("link", name=re.compile("Cookie", re.IGNORECASE))
        ).last

    @property
    def consent_banner(self) -> Locator:
        return self.page.locator("[aria-label*='consent'], .cookie-banner, .consent-banner")
