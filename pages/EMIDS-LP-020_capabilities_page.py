"""Page object for Capabilities section - EMIDS-LP-020, EMIDS-LP-021, EMIDS-LP-022, EMIDS-LP-023"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-020_capabilities_locators import CapabilitiesLocators


class CapabilitiesPage:
    """Page object for Capabilities section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CapabilitiesLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def verify_all_capability_groups(self) -> None:
        expect(self.locators.ai_card).to_be_visible()
        expect(self.locators.engineering_card).to_be_visible()
        expect(self.locators.platforms_card).to_be_visible()

    def get_capability_group_names(self) -> list[str]:
        groups = []
        for group in [self.locators.ai_card, self.locators.engineering_card, self.locators.platforms_card]:
            text = group.text_content()
            if text:
                groups.append(text.strip())
        return groups
