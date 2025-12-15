from playwright.sync_api import Page,expect
from pages.product_page import Product

def test_on_product_page(test_login_user, page:Page):
    pp=Product(page)
    # print("\nAVAILAVLE NOW------->>> backpack, bike, tshirt <<<---------AVAILAVLE NOW ")
    # prod_name=input("Enter your choosen product name to add in cart:-  ")
    pp.add_to_cart('tshirt')
    pp.add_to_cart('bike')
    pp.add_to_cart('backpack')
    # pp.add_to_cart(prod_name)
    expect(pp.cart_count,"Your Cart is Empty !!").to_be_attached()
    pp.cart_icon.click()
    expect(page.locator('.title')).to_have_text("Your Cart")