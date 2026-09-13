"""Page object for Hero messaging and visual rendering (issue_0009)."""
from playwright.sync_api import Page

from locators.issue_0009_hero_messaging_locators import HeroMessagingLocators


class HeroMessagingPage:
    """Page object for Hero section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeroMessagingLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def scroll_to_top(self) -> None:
        self.page.evaluate("() => window.scrollTo(0, 0)")

    def count_h1_elements(self) -> int:
        return self.locators.h1_elements.count()
