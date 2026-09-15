"""Locators for issue_0001: Homepage loads without errors."""
from playwright.sync_api import Page, Locator


class HomepageLoadingLocators:
    """Locators for the emids.com homepage."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def logo(self) -> Locator:
        return self.page.locator("img[alt*='Emids']")

    @property
    def main_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="In Healthcare, Only Outcomes Matter")

    @property
    def cookie_consent_banner(self) -> Locator:
        return self.page.locator("text=This website uses cookies")

    @property
    def allow_all_button(self) -> Locator:
        return self.page.get_by_role("button", name="Allow all")
