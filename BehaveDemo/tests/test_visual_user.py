from playwright.sync_api import Page,expect
from pages.product_page import Product

def test_visual_err_cls(login_user, page:Page):
    login_user("visual")
    product=Product(page)
    product.validate_products_page_loaded()

    expect(product.cart_icon_for_visual_user).to_contain_class("visual_failure")
