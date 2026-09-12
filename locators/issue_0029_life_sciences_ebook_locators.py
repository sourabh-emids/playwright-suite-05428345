"""Locators for issue_0029 - Life Sciences transformation eBook card display."""
from playwright.sync_api import Locator


class Issue0029LifeSciencesEbookLocators:
    """Locators for Life Sciences eBook card."""

    @property
    def life_sciences_card(self) -> Locator:
        """Return the Life Sciences eBook card."""
        return self.page.get_by_role("link", name="Unlocking Trusted Digital Transformation in Life Sciences")
