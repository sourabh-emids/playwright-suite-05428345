"""Locators for issue_0030 - AI ROI eBook card display."""
from playwright.sync_api import Locator


class Issue0030AiroiEbookLocators:
    """Locators for AI ROI eBook card."""

    @property
    def ai_roi_card(self) -> Locator:
        """Return the AI ROI eBook card."""
        return self.page.get_by_role("link", name="Closing the AI ROI Gap in Healthcare")
