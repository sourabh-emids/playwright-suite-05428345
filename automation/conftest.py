import os

import pytest
from playwright.sync_api import Page

from pages.tc_01_tc_02_tc_03_tc_04_tc_05_emids_page import EmidsPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
    }


@pytest.fixture(scope="session")
def emids_base_url() -> str:
    return os.getenv("EMIDS_BASE_URL", "https://www.emids.com").rstrip("/")


@pytest.fixture
def emids_page(page: Page, emids_base_url: str) -> EmidsPage:
    return EmidsPage(page, emids_base_url)
