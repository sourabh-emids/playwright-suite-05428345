"""Locators for issue_0027 - Medicare Advantage eBook card display."""
from playwright.sync_api import Locator


class Issue0027MedicareAdvantageEbookLocators:
    """Locators for Medicare Advantage eBook card."""

    @property
    def medicare_advantage_card(self) -> Locator:
        """Return the Medicare Advantage eBook card."""
        return self.page.get_by_role("link", name="Managing the Margin Reset in Medicare Advantage")
