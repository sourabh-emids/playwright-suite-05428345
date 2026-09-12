"""Locators for issue_0028 - CMS-0057 interoperability resource card display."""
from playwright.sync_api import Locator


class Issue0028CMS0057InteroperabilityLocators:
    """Locators for CMS-0057 interoperability card."""

    @property
    def cms0057_card(self) -> Locator:
        """Return the CMS-0057 eBook card."""
        return self.page.get_by_role("link", name="CMS-0057: The Interoperability Imperative")
