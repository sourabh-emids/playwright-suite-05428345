"""Page object for emids_lp_024: Render five audience industry entries."""
from playwright.sync_api import Page, expect
from locators.emids_lp_014_global_locators import WhoWeServeLocators


class WhoWeServePage:
    """Who We Serve section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = WhoWeServeLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to Who We Serve section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_audience_tabs(self) -> list[str]:
        """Get audience tab names."""
        tabs = []
        for loc in [self.locators.payer_tab, self.locators.provider_tab,
                    self.locators.healthtech_tab, self.locators.life_sciences_tab,
                    self.locators.consumer_tab]:
            try:
                if loc.is_visible():
                    tabs.append(loc.inner_text())
            except Exception:
                pass
        return tabs

    def get_audience_count(self) -> int:
        """Get count of audience tabs."""
        count = 0
        for loc in [self.locators.payer_tab, self.locators.provider_tab,
                    self.locators.healthtech_tab, self.locators.life_sciences_tab,
                    self.locators.consumer_tab]:
            try:
                if loc.is_visible():
                    count += 1
            except Exception:
                pass
        return count

    def click_audience_tab(self, name: str) -> None:
        """Click an audience tab."""
        name_lower = name.lower()
        if "payer" in name_lower:
            self.locators.payer_tab.click()
        elif "provider" in name_lower:
            self.locators.provider_tab.click()
        elif "healthtech" in name_lower or "health tech" in name_lower:
            self.locators.healthtech_tab.click()
        elif "life sciences" in name_lower:
            self.locators.life_sciences_tab.click()
        elif "consumer" in name_lower:
            self.locators.consumer_tab.click()

    def get_expected_urls(self) -> dict:
        """Get expected canonical URLs."""
        return {
            "payer": "/segments/payer/",
            "provider": "/segments/provider/",
            "healthtech": "/segments/healthtech/",
            "life_sciences": "/segments/life-sciences/",
            "consumer": "/segments/consumer/",
        }
