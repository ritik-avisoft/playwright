from playwright.sync_api import Page,expect
import pytest
from pages.login_page import login
from pages.product_page import Product
from utils.test_data import Test_data as td


@pytest.fixture
def open_app(page):
    page.goto("https://www.saucedemo.com/")
    return page

@pytest.fixture
def login_standard_user(open_app):
    login(open_app).logged_in(td.USERS[0], td.PASSWORD)
    return open_app

@pytest.fixture
def login_locked_user(open_app):
    login(open_app).logged_in(td.USERS[1], td.PASSWORD)
    return open_app

@pytest.fixture
def login_problem_user(open_app):
    login(open_app).logged_in(td.USERS[2], td.PASSWORD)
    return open_app

@pytest.fixture
def login_performance_glitch_user(open_app):
    login(open_app).logged_in(td.USERS[3], td.PASSWORD)
    return open_app



# @pytest.fixture
# def cart_ready(page):
#     lp = login(page)
#     lp.logged_in(td.USERS[0], td.PASSWORD)
#     pp = Product(page)
#     pp.add_to_cart("tshirt")
#     pp.add_to_cart("bike")
#     pp.add_to_cart("backpack")
#     return page
