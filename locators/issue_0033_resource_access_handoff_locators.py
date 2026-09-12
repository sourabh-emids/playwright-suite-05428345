"""Locators for issue_0033 - Resource access handoff for eBook cards."""
from playwright.sync_api import Locator


class Issue0033ResourceAccessHandoffLocators:
    """Locators for resource access handoff."""

    @property
    def ebook_card(self) -> Locator:
        """Return an eBook card."""
        return self.page.get_by_role("link", name="Managing the Margin Reset in Medicare Advantage")
