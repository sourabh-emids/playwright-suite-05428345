"""Shared behavior every generated page object inherits.

Locators are exposed as properties that return a fresh `Locator`, never a
resolved element -- so every use re-queries the live page and benefits from
Playwright's web-first auto-waiting instead of pointing at a stale node.
"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str) -> None:
        self.page.goto(path)

    def dismiss_cookie_consent_if_present(self) -> None:
        """Dismiss the inspected public-site consent overlay when it is shown."""
        allow_all = self.page.get_by_role("button", name="Allow all")
        if allow_all.is_visible(timeout=2_000):
            allow_all.click()
