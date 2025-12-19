from playwright.sync_api import Page, expect
from pages.product_page import Product
from utils.test_data import Test_data as td


def test_problem_user_images_are_same(login_user, page:Page):
    login_user("problem")
    product_page=Product(page)
    product_page.validate_img_for_problem_user()
