from playwright.sync_api import Page,expect

def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #using Xpath
    username=page.wait_for_selector('//input[@name="username"]')
    username.type("Admin")

    password=page.wait_for_selector('//input[@placeholder="Password"]')
    password.type("admin123")

    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(5000)