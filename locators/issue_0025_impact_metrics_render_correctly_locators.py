"""Locators for issue_0025: Impact metrics render correctly"""

from playwright.sync_api import Page, Locator


class Issue0025ImpactLocators:
    """Locators for Impact section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def impact_section(self) -> Locator:
        """Returns the Impact section."""
        return self.page.get_by_text("Impact")

    @property
    def metrics_text(self) -> Locator:
        """Returns metrics text."""
        return self.page.get_by_text("36+ Years Healthcare Experience")
