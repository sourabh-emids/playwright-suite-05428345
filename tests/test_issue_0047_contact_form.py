"""Test runner for issues 0047-0055: Contact, Accessibility, SEO, Performance, and Modal Modules."""
from pytest_bdd import scenarios
from tests.steps.issue_0047_contact_form_steps import *
from tests.steps.common_steps import *

scenarios("issue_0047_contact_form.feature")
