# import re
from playwright.sync_api import Page,expect
import pytest

def test_click_elements(page : Page):
    page.goto("https://demoqa.com/")

    page.locator(".card", has=page.get_by_role("heading", name="Elements")).click()
    expect(page).to_have_url("https://demoqa.com/elements")
    page.wait_for_timeout(3000)

