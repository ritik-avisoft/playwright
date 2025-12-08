from playwright.sync_api import Page,expect
import pytest
import re

@pytest.fixture
def landingpage(page:Page):
    page.goto("https://ultimateqa.com/automation/")
    print("Landing Page loaded Successfully")

    expect(page).to_have_title(re.compile("Automation Practice"))
    print("Page has title Automation ")
    page.wait_for_timeout(5000)
    return page