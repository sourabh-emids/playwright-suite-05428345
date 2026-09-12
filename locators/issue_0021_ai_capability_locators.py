"""Locators for issue_0021 - AI capability content rendering and links."""
from playwright.sync_api import Locator


class Issue0021AICapabilityLocators:
    """Locators for AI capability."""

    @property
    def ai_capability_section(self) -> Locator:
        """Return the AI capability section."""
        return self.page.locator("text=AI").first

    @property
    def ai_links(self) -> Locator:
        """Return AI-related links."""
        return self.page.locator("a:has-text('AI'), a:has-text('Agentic')")
