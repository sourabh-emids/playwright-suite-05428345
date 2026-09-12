"""Locators for issue_0013 - See the model CTA routing and operation."""
from playwright.sync_api import Locator


class Issue0013SeeModelCTALocators:
    """Locators for See the model CTA."""

    @property
    def see_model_cta(self) -> Locator:
        """Return the See the model CTA link."""
        return self.page.get_by_role("link", name="See the model")
