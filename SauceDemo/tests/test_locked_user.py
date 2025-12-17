from playwright.sync_api import Page,expect
from pages.login_page import login

def test_locked_user_verification(login_user,page:Page):
    login_user("locked")
    login_page = login(page)
    expect(login_page.login_err,"😭: Sorry, this user has been locked out.").to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")
