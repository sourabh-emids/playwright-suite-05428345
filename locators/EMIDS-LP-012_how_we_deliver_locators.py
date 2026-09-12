"""Locators for How We Deliver section - EMIDS-LP-012, EMIDS-LP-013"""
from playwright.sync_api import Page, Locator


class HowWeDeliverLocators:
    """Locators for How We Deliver section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("Forward-deployed context engineering turns ambition")

    @property
    def section_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Forward-Deployed Context Engineering")

    @property
    def see_the_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")

    @property
    def pacca_ai_foundry(self) -> Locator:
        return self.page.get_by_text("Pacca AI Foundry")

    @property
    def healthcare_ontology(self) -> Locator:
        return self.page.get_by_text("Healthcare Ontology")

    @property
    def strategic_alliances(self) -> Locator:
        return self.page.get_by_text("Strategic Alliances")
