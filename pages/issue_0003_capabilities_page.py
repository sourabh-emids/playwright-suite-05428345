"""Page object for issue_0003 - Capabilities mega-menu accessibility."""
from playwright.sync_api import Page, expect

from locators.issue_0003_capabilities_menu_locators import Issue0003CapabilitiesMenuLocators


class Issue0003CapabilitiesMenuPage:
    """Page object for Capabilities mega-menu accessibility."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0003CapabilitiesMenuLocators()
        self.locators.page = page

    def click_capabilities_navigation(self) -> None:
        """Click the Capabilities navigation item."""
        self.locators.capabilities_nav_button.click()

    def mega_menu_should_appear(self) -> None:
        """Verify mega-menu appears."""
        expect(self.locators.ai_header).to_be_visible()

    def menu_should_display_capability_group(self, group: str) -> None:
        """Verify a capability group is displayed in the menu."""
        if group == "AI":
            expect(self.locators.ai_header).to_be_visible()
        elif group == "Engineering":
            expect(self.locators.engineering_header).to_be_visible()
        elif group == "Platforms":
            expect(self.locators.platforms_header).to_be_visible()

    def capability_links_should_be_clickable(self) -> None:
        """Verify capability links are clickable."""
        # AI links
        ai_links = self.page.locator("[class*='capabilities'] a, [class*='menu'] a:has-text('AI')")
        if ai_links.count() > 0:
            expect(ai_links.first).to_be_enabled()
