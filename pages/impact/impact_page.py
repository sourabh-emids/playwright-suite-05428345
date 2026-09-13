"""Page object for Impact section."""
from playwright.sync_api import Page, expect
from locators.emids_lp_025_impact_locators import ImpactLocators


class ImpactPage:
    """Impact section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ImpactLocators(page)

    def navigate(self) -> None:
        """Navigate to homepage."""
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        """Scroll to Impact section."""
        self.locators.section_heading.scroll_into_view_if_needed()

    def get_metric_count(self) -> int:
        """Get count of visible metrics."""
        count = 0
        for loc in [self.locators.years_experience, self.locators.lives_touched,
                   self.locators.costs_saved, self.locators.platforms_launched]:
            try:
                if loc.is_visible():
                    count += 1
            except Exception:
                pass
        return count

    def get_metrics(self) -> dict:
        """Get all metric values and labels."""
        metrics = {}
        try:
            if self.locators.years_experience.is_visible():
                metrics["years"] = self.locators.years_experience.inner_text()
        except Exception:
            pass
        try:
            if self.locators.lives_touched.is_visible():
                metrics["lives"] = self.locators.lives_touched.inner_text()
        except Exception:
            pass
        try:
            if self.locators.costs_saved.is_visible():
                metrics["costs"] = self.locators.costs_saved.inner_text()
        except Exception:
            pass
        try:
            if self.locators.platforms_launched.is_visible():
                metrics["platforms"] = self.locators.platforms_launched.inner_text()
        except Exception:
            pass
        return metrics
