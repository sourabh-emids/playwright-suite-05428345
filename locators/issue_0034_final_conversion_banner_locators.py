"""Locators for issue_0034 - Final conversion banner rendering and CTA."""
from playwright.sync_api import Locator


class Issue0034FinalConversionBannerLocators:
    """Locators for Final conversion banner."""

    @property
    def final_cta_banner(self) -> Locator:
        """Return the final CTA banner."""
        return self.page.locator("text=From workshop to agent to scale deployment")

    @property
    def connect_cta(self) -> Locator:
        """Return the Connect CTA in final banner."""
        return self.final_cta_banner.locator("..").get_by_role("link", name="Connect")
