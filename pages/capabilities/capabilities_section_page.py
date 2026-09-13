"""Page object for emids_lp_020: Render capabilities overview."""
from playwright.sync_api import Page, expect
from locators.emids_lp_014_global_locators import CapabilitiesSectionLocators


class CapabilitiesSectionPage:
    """Capabilities section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CapabilitiesSectionLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to Capabilities section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_capability_groups(self) -> list[str]:
        """Get capability group labels."""
        groups = []
        for loc in [self.locators.ai_group, self.locators.engineering_group,
                    self.locators.platforms_group]:
            try:
                if loc.is_visible():
                    groups.append(loc.inner_text())
            except Exception:
                pass
        return groups

    def are_all_groups_visible(self) -> bool:
        """Check if all three groups are visible."""
        return (
            self.locators.ai_group.is_visible()
            and self.locators.engineering_group.is_visible()
            and self.locators.platforms_group.is_visible()
        )
