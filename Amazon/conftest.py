from playwright.sync_api import Page
import pytest


@pytest.fixture
def goto_amazon(page:Page):
    page.goto("https://www.amazon.in/")
    return page