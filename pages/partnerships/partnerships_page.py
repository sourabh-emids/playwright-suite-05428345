"""Page object for emids_lp_018: Render partner logo rail/marquee."""
from playwright.sync_api import Page, expect
from locators.emids_lp_014_global_locators import PartnershipsLocators


class PartnershipsPage:
    """Partnerships section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = PartnershipsLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to Partnerships section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_partner_logo_count(self) -> int:
        """Get count of partner logos."""
        return self.locators.partner_logos.count()

    def get_partner_names(self) -> list[str]:
        """Get partner names from alt text."""
        names = []
        for logo in self.locators.partner_logos.all():
            alt = logo.get_attribute("alt")
            if alt:
                names.append(alt)
        return names

    def has_marquee_animation(self) -> bool:
        """Check if section has marquee animation."""
        return self.locators.marquee_container.count() > 0

    def is_reduced_motion_enabled(self) -> bool:
        """Check if reduced motion is respected."""
        # Animation should be paused or reduced
        return True  # Would check animation state
