"""Page object for How We Deliver section rendering (issue_0012)."""
from playwright.sync_api import Page

from locators.issue_0012_how_we_deliver_locators import HowWeDeliverLocators


class HowWeDeliverPage:
    """Page object for How We Deliver section functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HowWeDeliverLocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def scroll_to_section(self) -> None:
        self.locators.section_heading.scroll_into_view_if_needed()
