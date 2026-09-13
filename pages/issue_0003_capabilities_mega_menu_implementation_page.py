"""Page object for issue_0003: Capabilities mega-menu implementation"""

from playwright.sync_api import Page, expect

from locators.issue_0003_capabilities_mega_menu_implementation_locators import Issue0003CapabilitiesMenuLocators


class Issue0003CapabilitiesMenuPage:
    """Page object for Capabilities mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0003CapabilitiesMenuLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def open_capabilities_menu(self) -> None:
        """Open the Capabilities menu."""
        self.locators.capabilities_nav_button.click()

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})

    def verify_capability_groups_visible(self) -> None:
        """Verify all three capability groups are visible."""
        expect(self.locators.ai_heading).to_be_visible()
        expect(self.locators.engineering_heading).to_be_visible()
        expect(self.locators.platforms_heading).to_be_visible()

    def navigate_with_tab_key(self) -> None:
        """Navigate using Tab key."""
        self.page.keyboard.press("Tab")

    def navigate_with_arrow_keys(self) -> None:
        """Navigate using Arrow keys."""
        self.page.keyboard.press("ArrowDown")

    def get_capability_labels(self) -> list[str]:
        """Get all capability labels."""
        labels = []
        for text in ["AI", "Engineering", "Platforms"]:
            if self.page.get_by_text(text).first.is_visible():
                labels.append(text)
        return labels

    def check_duplicate_labels(self) -> bool:
        """Check if there are duplicate labels."""
        labels = self.get_capability_labels()
        return len(labels) == len(set(labels))
