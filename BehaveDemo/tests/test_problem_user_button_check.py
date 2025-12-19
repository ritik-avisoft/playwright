from playwright.sync_api import Page, expect
from pages.product_page import Product
from utils.test_data import Test_data as td


def test_add_and_remove_products(login_user, page: Page):
    login_user("problem")
    product = Product(page)
    product.validate_products_page_loaded()


    for product_name in td.PRODUCTS.keys():
        product.add_product(product_name)
    product.validate_product_count_for_problem_user()
    page.pause()



