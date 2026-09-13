"""Locators for issue_0013: See the model CTA functionality"""

from playwright.sync_api import Page, Locator


class Issue0013SeeModelCTALocators:
    """Locators for See the model CTA."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def see_model_cta(self) -> Locator:
        """Returns the See the model CTA."""
        return self.page.get_by_role("link", name="See the model")
