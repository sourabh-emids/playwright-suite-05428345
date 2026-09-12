"""Locators for issue_0025 - Four impact proof metrics rendering."""
from playwright.sync_api import Locator


class Issue0025FourImpactMetricsLocators:
    """Locators for Impact section."""

    @property
    def impact_section(self) -> Locator:
        """Return the Impact section."""
        return self.page.locator("text=Impact").first

    @property
    def metric_cards(self) -> Locator:
        """Return the metric cards."""
        return self.impact_section.locator("..").locator("[class*='metric'], [class*='stat'], article")
