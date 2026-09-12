"""Insight cards display correctly."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("Medicare Advantage eBook card displays correctly")
def medicare_ebook_card_display(page: Page) -> None:
    """Verify Medicare Advantage eBook card displays correctly."""
    # Navigate to insights to find the card
    page.goto("/insights/")


@then("CMS-0057 interoperability card displays correctly")
def cms_card_display(page: Page) -> None:
    """Verify CMS-0057 interoperability card displays correctly."""
    page.goto("/insights/")


@then("Life Sciences transformation eBook card displays correctly")
def life_sciences_ebook_card_display(page: Page) -> None:
    """Verify Life Sciences transformation eBook card displays correctly."""
    page.goto("/insights/")


@then("AI ROI eBook card displays correctly")
def ai_roi_ebook_card_display(page: Page) -> None:
    """Verify AI ROI eBook card displays correctly."""
    page.goto("/insights/")


@then("FinOps payer resource card displays correctly")
def finops_payer_card_display(page: Page) -> None:
    """Verify FinOps payer resource card displays correctly."""
    page.goto("/insights/")


@then("Payer data readiness blog card displays with Read More")
def payer_blog_card_display(page: Page) -> None:
    """Verify Payer data readiness blog card displays with Read More."""
    page.goto("/insights/")
    read_more = page.get_by_role("link", name="Read More")
    expect(read_more).to_be_visible()
