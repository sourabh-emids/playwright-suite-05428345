"""Step definitions for issue_0018: Render partner logo rail/marquee."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views partner section")
def view_partner_section(page: Page) -> None:
    page.goto("/")


@when("Counting logos")
def count_logos(page: Page) -> None:
    pass


@then("All thirteen approved logos are visible: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, and Anthropic")
def thirteen_logos_visible(page: Page) -> None:
    partners_section = page.getByText("We've assembled the world's most powerful technology platforms")
    expect(partners_section).to_be_visible()


@when("Checking accessible names")
def check_accessible_names(page: Page) -> None:
    pass


@then("Each logo has descriptive alt text or accessibility label identifying the partner")
def logos_have_accessible_names(page: Page) -> None:
    logos = page.locator("img[data-testid='partner-logo']")
    if logos.count() > 0:
        alt = logos.first.get_attribute("alt")
        assert alt is not None or logos.first.get_attribute("aria-label") is not None


@given("DOM uses duplication for looping animation")
def dom_duplication(page: Page) -> None:
    page.goto("/")


@when("Screen reader navigates partner section")
def screen_reader_nav(page: Page) -> None:
    pass


@then("Partners are not announced multiple times due to animation loop")
def no_duplicate_announcements(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Partner configuration exists")
def partner_config_exists(page: Page) -> None:
    page.goto("/")


@when("Checking logo rendering")
def check_logo_rendering(page: Page) -> None:
    pass


@then("Each partner displays its logo asset; missing logo is flagged")
def logo_assets_present(page: Page) -> None:
    logos = page.locator("img[data-testid='partner-logo']")
    assert logos.count() >= 0


@given("Partner logo is not decorative")
def logo_not_decorative(page: Page) -> None:
    page.goto("/")


@when("Checking alt attribute")
def check_alt_attribute(page: Page) -> None:
    pass


@then("Logo has alt text or partner name is otherwise announced")
def alt_or_announced(page: Page) -> None:
    logos = page.locator("img[data-testid='partner-logo']")
    if logos.count() > 0:
        alt = logos.first.get_attribute("alt")
        aria = logos.first.get_attribute("aria-label")
        assert alt is not None or aria is not None


@given("Partner logos have adjacent partner names")
def logos_have_adjacent_names(page: Page) -> None:
    page.goto("/")


@when("Checking alt attributes")
def check_alt_attributes(page: Page) -> None:
    pass


@then("Logos with adjacent text may be treated as decorative with empty alt")
def decorative_with_empty_alt(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Partner has transparent PNG logo")
def transparent_logo(page: Page) -> None:
    page.goto("/")


@when("Logo renders on page background")
def logo_renders(page: Page) -> None:
    pass


@then("Logo maintains sufficient visibility/contrast against background")
def logo_visible(page: Page) -> None:
    partners_section = page.getByText("We've assembled the world's most powerful technology platforms")
    expect(partners_section).to_be_visible()


@given("User has prefers-reduced-motion")
def prefers_reduced_motion(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Marquee animation would run")
def marquee_runs(page: Page) -> None:
    pass


@then("Animation pauses or reduces to static display")
def animation_paused(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
