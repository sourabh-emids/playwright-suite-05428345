"""Locators for How We Deliver section rendering (issue_0012)."""
from playwright.sync_api import Locator, Page


class HowWeDeliverLocators:
    """Locators for How We Deliver section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def section_text(self) -> Locator:
        return self.page.get_by_text("Forward-deployed context engineering turns ambition")

    @property
    def see_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model").first

    @property
    def how_we_deliver_section(self) -> Locator:
        return self.page.locator("text=Forward-deployed context engineering").locator("..")
