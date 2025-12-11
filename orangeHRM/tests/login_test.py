from playwright.sync_api import Page,expect
from pages.login_page import LoginPage  # imported the classses 

# def test_login(page:Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#     username=page.wait_for_selector('//input[@name="username"]')
#     username.type("Admin")
#     password=page.wait_for_selector('//input[@placeholder="Password"]')
#     password.type("admin123")
#     page.wait_for_selector('//button[@type="submit"]').click()

def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    login_page=LoginPage(page) # Created the obj of classes
    login_page.use_login("Admin", "admin123")