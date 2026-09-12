"""Locators for issue_0035 - Delivery timing message rendering."""
from playwright.sync_api import Locator


class Issue0035DeliveryTimingMessageLocators:
    """Locators for delivery timing message."""

    @property
    def timing_message(self) -> Locator:
        """Return the timing message."""
        return self.page.locator("text=1 Day · 2 Weeks · 3 Months")

    @property
    def timing_description(self) -> Locator:
        """Return the timing description."""
        return self.page.locator("text=One day. Two weeks. Three months. That's all it takes")
