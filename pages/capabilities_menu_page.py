"""Page object for the Capabilities Mega-Menu (issue_0003)."""
from playwright.sync_api import Page, expect
from locators.capabilities_menu_locators import CapabilitiesMenuLocators


class CapabilitiesMenuPage(CapabilitiesMenuLocators):
    """Page object for Capabilities mega-menu functionality."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open_capabilities_menu(self) -> None:
        self.capabilities_trigger.click()

    def close_capabilities_menu(self) -> None:
        self.capabilities_trigger.click()

    def press_escape(self) -> None:
        self.page.keyboard.press("Escape")

    def get_capability_link_count(self) -> int:
        return self.capability_links.count()

    def is_menu_open(self) -> bool:
        return self.capabilities_menu.is_visible()

    def get_group_labels(self) -> list:
        labels = []
        if self.ai_group.is_visible():
            labels.append("AI")
        if self.engineering_group.is_visible():
            labels.append("Engineering")
        if self.platforms_group.is_visible():
            labels.append("Platforms")
        return labels

    def click_capability_link(self, name: str) -> None:
        if name == "Digital Engineering":
            self.digital_engineering_link.click()
        elif name == "Low-Code":
            self.low_code_link.click()
