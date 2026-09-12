"""Page object for Impact section - EMIDS-LP-025"""
from playwright.sync_api import Page, expect
from locators.EMIDS-LP-025_impact_metrics_locators import ImpactLocators


class ImpactMetricsPage:
    """Page object for Impact section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ImpactLocators(page)

    def goto(self, path: str = "/") -> None:
        self.page.goto(path)

    def verify_section_visible(self) -> None:
        expect(self.locators.section).to_be_visible()

    def verify_all_metrics(self) -> None:
        expect(self.locators.years_experience_metric).to_be_visible()
        expect(self.locators.lives_touched_metric).to_be_visible()
        expect(self.locators.costs_saved_metric).to_be_visible()
        expect(self.locators.platforms_launched_metric).to_be_visible()

    def count_metrics(self) -> int:
        return self.locators.all_metrics.count()

    def verify_special_characters(self) -> None:
        metric_text = self.locators.costs_saved_metric.text_content()
        expect(metric_text).to_contain_text("$")
