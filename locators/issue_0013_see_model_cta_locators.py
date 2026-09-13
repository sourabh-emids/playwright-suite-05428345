"""Locators for See the model CTA functionality (issue_0013)."""
from playwright.sync_api import Locator, Page


class SeeModelCTALocators:
    """Locators for See the model CTA elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def see_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model").first
