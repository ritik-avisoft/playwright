from playwright.sync_api import Page,expect
from pages.info_page import InfoPage
from pages.login_page import LoginPage

def test_get_user_name(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page=LoginPage(page)
    login_page.use_login("Admin","admin123")
    get_u_name=InfoPage(page)
    get_u_name.get_name()