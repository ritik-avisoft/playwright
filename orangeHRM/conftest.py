from playwright.sync_api import Page,expect
import pytest

@pytest.fixture
def login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #using Xpath
    username=page.wait_for_selector('//input[@name="username"]')
    username.type("Admin")

    password=page.wait_for_selector('//input[@placeholder="Password"]')
    password.type("admin123")

    page.wait_for_selector('//button[@type="submit"]').click()
    print("->> Login Successfully..")
    page.wait_for_timeout(3000)
    return page