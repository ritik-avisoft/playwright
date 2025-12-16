from playwright.sync_api import Page,expect
from pages.product_page import Product
from pages.cart_page import Cart

# def test_error_user_sort_shows_alert(login_error_user, page):
#     product_page = Product(page)
#     def dialog_handler(dialog):
#         assert "Sorting is broken! This error has been reported to Backtrace." in dialog.message
#         dialog.accept()

#     page.on("dialog", dialog_handler)

#     product_page.sort_product.select_option("lohi")

def test_order_place(login_error_user,page:Page):
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
    #check that input is now enable 
    # expect(cart_page.f_name).to_be_editable()

    expect(cart_page.f_name).to_have_value("Ritik")
    # cart_page.l_name.type("ranjan")
    expect(cart_page.l_name).not_to_have_value("Ranjan")

    cart_page.continue_order_btn.click()


    # expect(cart_page.err_msg_container).to_be_visible()
    # expect(cart_page.err_msg_container).to_contain_text("Error: Last Name is required")
