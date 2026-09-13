"""Page object for issue_0024: Five audience entries render"""

from playwright.sync_api import Page, expect

from locators.issue_0024_five_audience_entries_render_locators import Issue0024WhoWeServeLocators


class Issue0024WhoWeServePage:
    """Page object for Who We Serve section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0024WhoWeServeLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_all_audiences(self) -> None:
        """Verify all five audiences are visible."""
        expect(self.locators.payer_button).to_be_visible()
        expect(self.locators.provider_button).to_be_visible()
        expect(self.locators.healthtech_button).to_be_visible()
        expect(self.locators.life_sciences_button).to_be_visible()
        expect(self.locators.consumer_button).to_be_visible()

    def count_audiences(self) -> int:
        """Count the number of audience buttons."""
        return self.page.get_by_role("button", name="Payer").count() + \
               self.page.get_by_role("button", name="Provider").count() + \
               self.page.get_by_role("button", name="HealthTech").count() + \
               self.page.get_by_role("button", name="Life Sciences").count() + \
               self.page.get_by_role("button", name="Consumer").count()

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})
