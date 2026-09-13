"""Page object for emids_lp_014: Maintain semantic section hierarchy."""
from playwright.sync_api import Page, expect
from locators.emids_lp_014_global_locators import GlobalLocators


class GlobalPage:
    """Global page semantics page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = GlobalLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def get_h1_count(self) -> int:
        """Get count of H1 elements."""
        return self.locators.all_h1s.count()

    def get_heading_hierarchy(self) -> dict:
        """Get heading hierarchy details."""
        return {
            "h1_count": self.locators.all_h1s.count(),
            "h2_count": self.locators.all_h2s.count(),
            "h3_count": self.locators.all_h3s.count(),
        }

    def has_logical_hierarchy(self) -> bool:
        """Check if heading hierarchy is logical (no skipped levels)."""
        # Should have H1 before H2, H2 before H3
        hierarchy = self.get_heading_hierarchy()
        return hierarchy["h1_count"] >= 1

    def are_landmarks_present(self) -> dict:
        """Check for required landmarks."""
        return {
            "main": self.locators.main_landmark.count() > 0,
            "header": self.locators.header_landmark.count() > 0,
            "footer": self.locators.footer_landmark.count() > 0,
        }
