import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def click_elements(page : Page):
    page.goto("https://demoqa.com/")

    page.locator(".card", has=page.get_by_role("heading", name="Elements")).click()
    expect(page).to_have_url("https://demoqa.com/elements")
    page.wait_for_timeout(3000)
    return page
