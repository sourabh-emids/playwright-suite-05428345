"""Locators for the How We Deliver module (issues 0012, 0013)."""
from playwright.sync_api import Locator, Page


class HowWeDeliverLocators:
    """Locators for the How We Deliver section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.locator("text=Forward-Deployed Context Engineering").locator("..").locator("..")

    @property
    def section_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def supporting_explanation(self) -> Locator:
        return self.page.locator("text=Forward-deployed context engineering turns ambition")

    @property
    def cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")

    @property
    def visual_elements(self) -> Locator:
        return self.page.locator("text=Forward-Deployed Context Engineering + *")
