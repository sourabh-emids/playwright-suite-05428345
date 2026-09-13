"""Locators for issue_0003: Capabilities mega-menu implementation"""

from playwright.sync_api import Page, Locator


class Issue0003CapabilitiesMenuLocators:
    """Locators for the Capabilities mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_nav_button(self) -> Locator:
        """Returns the Capabilities navigation button."""
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def ai_heading(self) -> Locator:
        """Returns the AI heading."""
        return self.page.get_by_text("AI")

    @property
    def engineering_heading(self) -> Locator:
        """Returns the Engineering heading."""
        return self.page.get_by_text("Engineering")

    @property
    def platforms_heading(self) -> Locator:
        """Returns the Platforms heading."""
        return self.page.get_by_text("Platforms")

    @property
    def capabilities_menu(self) -> Locator:
        """Returns the Capabilities menu container."""
        return self.page.locator("button:has-text('Capabilities') + *")

    def get_capability_links_in_group(self, group_name: str) -> Locator:
        """Returns capability links within a specific group."""
        return self.page.get_by_text(group_name).locator("..").locator("a")
