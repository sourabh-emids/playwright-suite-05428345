"""Locators for the Contact page."""
from playwright.sync_api import Locator, Page


class ContactPageLocators:
    """Locators for the Emids contact page."""
    
    def __init__(self, page: Page):
        self.page = page
    
    # Contact form
    @property
    def contact_form(self) -> Locator:
        return self.page.locator("form").first
    
    @property
    def first_name_field(self) -> Locator:
        return self.page.locator('input[name*="first"], input[id*="first"], input[placeholder*="First"]').first
    
    @property
    def last_name_field(self) -> Locator:
        return self.page.locator('input[name*="last"], input[id*="last"], input[placeholder*="Last"]').first
    
    @property
    def email_field(self) -> Locator:
        return self.page.locator('input[type="email"], input[name*="email"], input[id*="email"]').first
    
    @property
    def company_field(self) -> Locator:
        return self.page.locator('input[name*="company"], input[id*="company"], input[placeholder*="Company"]').first
    
    @property
    def title_field(self) -> Locator:
        return self.page.locator('input[name*="title"], input[id*="title"], input[placeholder*="Title"]').first
    
    @property
    def phone_field(self) -> Locator:
        return self.page.locator('input[type="tel"], input[name*="phone"], input[id*="phone"]').first
    
    @property
    def inquiry_type_select(self) -> Locator:
        return self.page.locator('select[name*="inquiry"], select[id*="inquiry"], select[aria-label*="Inquiry"]').first
    
    @property
    def comments_field(self) -> Locator:
        return self.page.locator('textarea[name*="comment"], textarea[name*="message"], textarea[id*="comment"], textarea[placeholder*="Comment"]').first
    
    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")
    
    # Inquiry type options
    @property
    def inquiry_type_services(self) -> Locator:
        return self.page.locator('select option, [role="option"]').filter(has_text="Services")
    
    @property
    def inquiry_type_careers(self) -> Locator:
        return self.page.locator('select option, [role="option"]').filter(has_text="Careers")
    
    @property
    def inquiry_type_employment(self) -> Locator:
        return self.page.locator('select option, [role="option"]').filter(has_text="Employment Verification")
    
    @property
    def inquiry_type_media(self) -> Locator:
        return self.page.locator('select option, [role="option"]').filter(has_text="Media Request")
    
    @property
    def inquiry_type_other(self) -> Locator:
        return self.page.locator('select option, [role="option"]').filter(has_text="Other")
    
    # Form labels
    @property
    def first_name_label(self) -> Locator:
        return self.page.getByText("First Name", exact=False).first
    
    @property
    def last_name_label(self) -> Locator:
        return self.page.getByText("Last Name", exact=False).first
    
    @property
    def email_label(self) -> Locator:
        return self.page.getByText("Email", exact=False).first
    
    @property
    def company_label(self) -> Locator:
        return self.page.getByText("Company", exact=False).first
    
    @property
    def title_label(self) -> Locator:
        return self.page.getByText("Title", exact=False).first
    
    @property
    def phone_label(self) -> Locator:
        return self.page.getByText("Phone", exact=False).first
    
    @property
    def inquiry_type_label(self) -> Locator:
        return self.page.getByText("Inquiry Type", exact=False).first
    
    @property
    def comments_label(self) -> Locator:
        return self.page.getByText("Comments", exact=False).first
    
    # Form validation messages
    @property
    def form_error_messages(self) -> Locator:
        return self.page.locator('[class*="error"], [class*="invalid"], [role="alert"]')
    
    @property
    def success_message(self) -> Locator:
        return self.page.locator('[class*="success"], [class*="thank"], [role="status"]').first
    
    # Privacy policy link
    @property
    def privacy_policy_link(self) -> Locator:
        return self.page.getByText("privacy policy", exact=False)
    
    # Office locations
    @property
    def offices_section(self) -> Locator:
        return self.page.getByText("Locations", exact=False).first
    
    @property
    def north_america_tab(self) -> Locator:
        return self.page.getByText("North America", exact=False).first
    
    @property
    def asia_tab(self) -> Locator:
        return self.page.getByText("Asia", exact=False).first
    
    @property
    def europe_tab(self) -> Locator:
        return self.page.getByText("Europe", exact=False).first
    
    # Contact info
    @property
    def contact_email(self) -> Locator:
        return self.page.locator('a[href^="mailto:"]').first
    
    @property
    def contact_phone(self) -> Locator:
        return self.page.locator('a[href^="tel:"]').first
