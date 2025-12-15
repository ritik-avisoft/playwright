from playwright.sync_api import Page,expect
from pages.product_page import Product
from pages.cart_page import Cart

def test_standard_user_add_to_cart(test_login_user, page: Page):
    product_page = Product(page)
    product_page.add_to_cart('tshirt')
    product_page.add_to_cart('bike')
    product_page.add_to_cart('backpack')
    # Assert cart badge is visible
    expect(product_page.cart_count).to_be_visible()
    # Assert correct item count
    expect(product_page.cart_count).to_have_text("3")
    print("Products added successfully")


def test_sort_product(test_login_user, page: Page):
    pp = Product(page)
    pp.sort_product_by("az")

    
def test_standred_user_order_confirmation(test_login_user,page:Page):
    product_page=Product(page)
    cart_page=Cart(page)

    product_page.add_to_cart('bike')
    product_page.add_to_cart('backpack')
    expect(product_page.cart_count,"Your Cart is Empty !!").to_be_attached()
    product_page.cart_icon.click()

    #assert the you are on cart page
    expect(cart_page.cart_page_header_title, "you are not on the cart page").to_be_visible()
    cart_page.cart_checkout_button.click()
    #call method to fill details 
    cart_page.your_info("Ritik", "Ranjan", "450054")
    #confirming the order amount
    cart_page.order_overview()
    #order placing
    cart_page.cart_finish_btn.click()
    #asserting that order is confirmed.
    expect(cart_page.cart_order_complete).to_be_visible()

    






