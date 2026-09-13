"""Page object for Capabilities mega-menu implementation (issue_0003)."""
from playwright.sync_api import Page

from locators.issue_0003_capabilities_megamenu_locators import CapabilitiesMegamenuLocators


class CapabilitiesMegamenuPage:
    """Page object for Capabilities mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CapabilitiesMegamenuLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def activate_capabilities(self) -> None:
        self.locators.capabilities_button.hover()
        self.page.wait_for_timeout(300)

    def click_capabilities(self) -> None:
        self.locators.capabilities_button.click()

    def is_menu_open(self) -> bool:
        try:
            return self.locators.menu_visible.is_visible()
        except Exception:
            return False

    def get_capability_groups(self) -> list:
        return [
            self.locators.ai_group,
            self.locators.engineering_group,
            self.locators.platforms_group,
        ]

    def get_capability_links(self) -> list:
        return self.locators.capability_links.all()
