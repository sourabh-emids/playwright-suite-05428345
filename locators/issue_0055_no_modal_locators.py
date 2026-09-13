"""Locators for No promotional modal in base experience (issue_0055)."""
from playwright.sync_api import Locator, Page


class NoModalLocators:
    """Locators for no modal elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def modal(self) -> Locator:
        return self.page.locator("[role='dialog'], .modal, .popup")

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")
