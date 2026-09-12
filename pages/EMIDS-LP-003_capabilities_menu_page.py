"""Page object for Capabilities mega-menu - EMIDS-LP-003"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-003_capabilities_menu_locators import CapabilitiesMenuLocators


class CapabilitiesMenuPage:
    """Page object for Capabilities mega-menu functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CapabilitiesMenuLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def open_capabilities_menu(self) -> None:
        self.locators.capabilities_trigger.click()

    def get_capability_groups(self) -> list[str]:
        groups = []
        expect(self.locators.ai_group).to_be_visible()
        groups.append("AI")
        expect(self.locators.engineering_group).to_be_visible()
        groups.append("Engineering")
        expect(self.locators.platforms_group).to_be_visible()
        groups.append("Platforms")
        return groups

    def tab_through_menu_items(self) -> list[str]:
        focused = []
        self.locators.capabilities_trigger.click()
        for _ in range(self.locators.capability_links.count() + 5):
            self.page.keyboard.press("Tab")
            focused.append(self.page.evaluate("document.activeElement.tagName"))
        return focused

    def verify_group_labels(self) -> None:
        expect(self.locators.ai_group).to_be_visible()
        expect(self.locators.engineering_group).to_be_visible()
        expect(self.locators.platforms_group).to_be_visible()
