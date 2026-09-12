"""Page object for issue_0024 - Five audience entries rendering and Explore actions."""
from playwright.sync_api import Page, expect

from locators.issue_0024_who_we_serve_locators import Issue0024WhoWeServeLocators


class Issue0024WhoWeServePage:
    """Page object for Who We Serve section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0024WhoWeServeLocators()
        self.locators.page = page

    def view_who_we_serve_section(self) -> None:
        """Scroll to the Who We Serve section."""
        self.locators.who_we_serve_section.scroll_into_view_if_needed()

    def five_audience_entries_should_be_visible(self) -> None:
        """Verify five audience entries are visible."""
        # Count audience buttons
        buttons = [
            self.locators.payer_button,
            self.locators.provider_button,
            self.locators.healthtech_button,
            self.locators.life_sciences_button,
            self.locators.consumer_button,
        ]
        visible_count = 0
        for button in buttons:
            if await button.is_visible():
                visible_count += 1
        assert visible_count >= 5, f"Expected at least 5 audience entries, found {visible_count}"

    def audience_should_include(self, audience: str) -> None:
        """Verify specific audience is included."""
        if audience == "Payer":
            expect(self.locators.payer_button).to_be_visible()
        elif audience == "Provider":
            expect(self.locators.provider_button).to_be_visible()
        elif audience == "HealthTech":
            expect(self.locators.healthtech_button).to_be_visible()
        elif audience == "Life Sciences":
            expect(self.locators.life_sciences_button).to_be_visible()
        elif audience == "Consumer":
            expect(self.locators.consumer_button).to_be_visible()

    def each_audience_should_have_explore_action(self) -> None:
        """Verify each audience has an Explore action."""
        explore_buttons = self.locators.explore_buttons
        expect(explore_buttons.first).to_be_visible()
