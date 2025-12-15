from playwright.sync_api import Page,expect
from pages.login_page import login
from utils.test_data import Test_data as td

def test_login_user(open_app):
    login_page = login(open_app)
    login_page.logged_in(td.USERS[0], td.PASSWORD)

def test_locked_out_user_login(open_app):
    login_page = login(open_app)
    login_page.logged_in(td.USERS[1], td.PASSWORD)
    expect(login_page.login_err,"😭: Sorry, this user has been locked out.").to_have_text("Epic sadface: Sorry, this user has been locked out.")

