"""Page object for Hero media loading optimization (issue_0011)."""
from playwright.sync_api import Page

from locators.issue_0011_hero_media_optimization_locators import HeroMediaOptimizationLocators


class HeroMediaOptimizationPage:
    """Page object for Hero media optimization functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeroMediaOptimizationLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def get_image_attributes(self) -> list:
        images = self.locators.hero_images.all()
        results = []
        for img in images:
            results.append({
                "src": img.get_attribute("src"),
                "srcset": img.get_attribute("srcset"),
                "sizes": img.get_attribute("sizes"),
                "loading": img.get_attribute("loading"),
            })
        return results
