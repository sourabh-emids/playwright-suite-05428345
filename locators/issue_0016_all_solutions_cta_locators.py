"""Locators for issue_0016 - All Solutions CTA visibility and routing."""
from playwright.sync_api import Locator


class Issue0016AllSolutionsCTALocators:
    """Locators for All Solutions CTA."""

    @property
    def all_solutions_cta(self) -> Locator:
        """Return the All solutions CTA link."""
        return self.page.get_by_role("link", name="All solutions")
