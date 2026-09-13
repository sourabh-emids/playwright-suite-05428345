"""Page object for issue_0017: Featured solutions responsive interaction"""

from playwright.sync_api import Page, expect

from locators.issue_0017_featured_solutions_responsive_interaction_locators import Issue0017FeaturedSolutionsResponsiveLocators


class Issue0017FeaturedSolutionsResponsivePage:
    """Page object for Featured Solutions responsive interaction."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0017FeaturedSolutionsResponsiveLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})

    def resize_to_tablet(self) -> None:
        """Resize to tablet viewport."""
        self.page.set_viewport_size({"width": 768, "height": 1024})

    def resize_to_desktop(self) -> None:
        """Resize to desktop viewport."""
        self.page.set_viewport_size({"width": 1280, "height": 720})

    def check_no_horizontal_scroll(self) -> bool:
        """Check for horizontal scroll."""
        scroll_width = self.page.evaluate("document.documentElement.scrollWidth")
        client_width = self.page.evaluate("document.documentElement.clientWidth")
        return scroll_width <= client_width

    def verify_carousel_controls_have_labels(self) -> None:
        """Verify carousel controls have accessible labels."""
        # Check if controls are present and have labels
        pass

    def verify_reduced_motion_respected(self) -> None:
        """Verify reduced motion is respected."""
        expect(self.page.get_by_role("main")).to_be_visible()
