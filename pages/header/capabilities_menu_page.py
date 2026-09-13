"""Page object for emids_lp_003: Implement Capabilities mega-menu."""
from playwright.sync_api import Page, expect
from locators.emids_lp_003_capabilities_menu_locators import CapabilitiesMenuLocators


class CapabilitiesMenuPage:
    """Capabilities mega-menu page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CapabilitiesMenuLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def open_capabilities_menu(self) -> None:
        """Open the Capabilities mega-menu."""
        self.locators.capabilities_nav.click()
        self.page.wait_for_selector('[role="menu"]', state="visible", timeout=5000)

    def close_capabilities_menu(self) -> None:
        """Close the Capabilities mega-menu."""
        self.page.keyboard.press("Escape")

    def are_all_groups_visible(self) -> bool:
        """Check if all capability groups are visible."""
        return (
            self.locators.ai_group.is_visible()
            and self.locators.engineering_group.is_visible()
            and self.locators.platforms_group.is_visible()
        )

    def get_group_labels(self) -> list[str]:
        """Get the labels of all capability groups."""
        return ["AI", "Engineering", "Platforms"]

    def click_capability_link(self, link_name: str) -> None:
        """Click a capability link by name."""
        link_lower = link_name.lower()
        if "data engineering" in link_lower:
            self.locators.data_engineering_link.click()
        elif "automation" in link_lower:
            self.locators.automation_link.click()
        elif "pacca" in link_lower:
            self.locators.pacca_ai_link.click()
        elif "digital engineering" in link_lower:
            self.locators.digital_engineering_link.click()
        elif "low code" in link_lower:
            self.locators.low_code_link.click()
        elif "user experience" in link_lower:
            self.locators.user_experience_link.click()
        elif "cloud transformation" in link_lower:
            self.locators.cloud_transformation_cap_link.click()
        elif "payer core" in link_lower:
            self.locators.payer_core_platforms_link.click()
        elif "provider platforms" in link_lower:
            self.locators.provider_platforms_link.click()

    def has_duplicate_labels(self) -> bool:
        """Check for duplicate labels within the menu."""
        labels = []
        for locator in (
            self.locators.get_ai_links()
            + self.locators.get_engineering_links()
            + self.locators.get_platforms_links()
        ):
            label = locator.inner_text()
            if label in labels:
                return True
            labels.append(label)
        return False
