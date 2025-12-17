import pytest
from pages.login_page import login
from utils.test_data import Test_data as td


@pytest.fixture
def open_app(page):
    page.goto("https://www.saucedemo.com/")
    return page

@pytest.fixture
def login_user(open_app):
    def _login(user_key: str):
        username = td.USERS[user_key]
        login(open_app).logged_in(username, td.PASSWORD_ENCRYPTED)
        return open_app
    return _login
