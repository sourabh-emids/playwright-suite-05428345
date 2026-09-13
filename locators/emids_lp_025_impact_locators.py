"""Locators for Impact section and remaining sections."""
from playwright.sync_api import Locator, Page


class ImpactLocators:
    """Impact section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Impact")

    @property
    def years_experience(self) -> Locator:
        """36+ Years Healthcare Experience."""
        return self.page.get_by_text("36+ Years", exact=True)

    @property
    def lives_touched(self) -> Locator:
        """115+ Million Lives Touched."""
        return self.page.get_by_text("115+ Million", exact=True)

    @property
    def costs_saved(self) -> Locator:
        """$48+ Billion Medical Costs Saved."""
        return self.page.get_by_text("$48+ Billion", exact=True)

    @property
    def platforms_launched(self) -> Locator:
        """450+ Platforms Launched."""
        return self.page.get_by_text("450+", exact=True)

    @property
    def all_metrics(self) -> Locator:
        """All metric elements."""
        return self.page.get_by_text("36+ Years", exact=True).locator("..").locator("..")


class InsightsLocators:
    """Insights section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("Insights")

    @property
    def insight_cards(self) -> Locator:
        """Insight cards."""
        return self.page.locator("[class*='insight'], [class*='card']").filter(
            has=self.page.get_by_role("heading")
        )

    @property
    def next_button(self) -> Locator:
        """Next carousel button."""
        return self.page.get_by_role("button", name="Next")


class FinalCTALocators:
    """Final CTA section locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section_heading(self) -> Locator:
        """Section heading."""
        return self.page.get_by_text("From workshop to agent to scale deployment")

    @property
    def timing_labels(self) -> Locator:
        """Timing labels: 1 Day, 2 Weeks, 3 Months."""
        return self.page.get_by_text("1 Day")

    @property
    def connect_cta(self) -> Locator:
        """Connect CTA."""
        return self.page.get_by_role("link", name="Connect").last


class ContactFormLocators:
    """Contact form locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def first_name(self) -> Locator:
        """First Name field."""
        return self.page.get_by_label("* First Name:")

    @property
    def last_name(self) -> Locator:
        """Last Name field."""
        return self.page.get_by_label("* Last Name:")

    @property
    def work_email(self) -> Locator:
        """Work Email field."""
        return self.page.get_by_label("* Work Email Address:")

    @property
    def company(self) -> Locator:
        """Company Name field."""
        return self.page.get_by_label("* Company Name:")

    @property
    def title_field(self) -> Locator:
        """Title field."""
        return self.page.get_by_label("Title:")

    @property
    def phone(self) -> Locator:
        """Phone Number field."""
        return self.page.get_by_label("Phone Number:")

    @property
    def inquiry_type(self) -> Locator:
        """Inquiry Type dropdown."""
        return self.page.get_by_label("* Inquiry Type:")

    @property
    def comments(self) -> Locator:
        """Comments field."""
        return self.page.get_by_label("Comments:")

    @property
    def submit_button(self) -> Locator:
        """Submit button."""
        return self.page.get_by_role("button", name="Submit")


class FooterLocators:
    """Footer locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def cookie_preferences(self) -> Locator:
        """Cookie Preferences control."""
        return self.page.get_by_role("link", name="Cookie Preferences")

    @property
    def privacy_policy(self) -> Locator:
        """Privacy Policy link."""
        return self.page.get_by_role("link", name="Privacy Policy")

    @property
    def cookie_policy(self) -> Locator:
        """Cookie Policy link."""
        return self.page.get_by_role("link", name="Cookie Policy")

    @property
    def accessibility_statement(self) -> Locator:
        """Accessibility Statement link."""
        return self.page.get_by_role("link", name="Accessibility Statement")

    @property
    def copyright(self) -> Locator:
        """Copyright text."""
        return self.page.get_by_text("Copyright")

    @property
    def social_links(self) -> Locator:
        """Social media links."""
        return self.page.locator("[class*='social'] a")
