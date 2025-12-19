from playwright.sync_api import Page,expect
from pages.product_page import Product

class Cart:
    def __init__(self,page:Page):
        self.page=page
        self.cart_page_header_title=page.get_by_text("Your Cart")
        self.cart_item_name=page.locator(".inventory_item_name")
        self.cart_item_count=page.locator(".cart_item")

        ## from the product page we can also get the remove btn by name
        self.cart_remove_btn=page.locator(".btn.btn_secondary.btn_small.cart_button")
        self.cart_checkout_button=page.locator('id=checkout')
        self.cart_back_to_shopping_button=page.locator(".btn btn_secondary.back.btn_medium")
        self.cart_finish_btn=page.locator('id=finish')
        self.cart_order_complete=page.get_by_text("Thank you for your order!")

        self.f_name=self.page.get_by_placeholder("First Name")
        self.l_name=self.page.get_by_placeholder("Last Name")
        self.zip=self.page.get_by_placeholder("Zip/Postal Code")
        self.continue_order_btn=self.page.locator('id=continue')

        self.err_msg_container=self.page.locator(".error-message-container.error")
       
    def open_cart_page(self):
        product_page=Product(self.page)
        product_page.cart_icon.click()        
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        
    def verify_cart_product(self):
        item =self.cart_item_name.all_text_contents()
        product_count=len(item)
        expected_total = self.cart_item_count.count()  
        # expect(product_count).to_have_count(expected_total)
        assert  product_count==expected_total , "Count mis matched!!"
            
    def product_added_to_cart(self,product_name:str):
        item_names = self.cart_item_name.all_text_contents()
        assert [True if product_name in item_name else False for item_name in item_names], f"{product_name} is not present in the cart" 

    def remove_product_from_cart(self,product_name:str):
        if product_name=="backpack":
            self.page.locator('id=remove-sauce-labs-backpack').click()
        elif product_name=="bike":
            self.page.locator('id=remove-sauce-labs-bike-light').click()
        elif product_name=="tshirt":
            self.page.locator('id=remove-sauce-labs-bolt-t-shirt').click()
        else:
            print("Product not found to remove from cart...")

    def your_info(self, first_name:str, last_name:str, zip:str):
        self.f_name.type(first_name,delay=200)
        self.l_name.type(last_name,delay=200)
        self.zip.type(zip, delay=200)
        self.continue_order_btn.click()
        # self.err_msg_container=self.page.locator(".error-message-container.error")
        return self.page
    
    def order_overview(self):
        item_prices = self.page.locator(".inventory_item_price")
        tax_label = self.page.locator(".summary_tax_label")
        total_label = self.page.locator(".summary_total_label")

        # Sum item prices
        sum_of_items = 0.0
        for price in item_prices.all_text_contents():
            price_value = float(price.replace("$", "").strip())
            sum_of_items += price_value

        # Extract tax
        tax_text = tax_label.text_content()  # "Tax: $8.48"
        tax_value = float(
            tax_text.replace("Tax:", "").replace("$", "").strip()
        )

        # Extract displayed total
        total_text = total_label.text_content()  # "Total: $114.44"
        displayed_total = float(
            total_text.replace("Total:", "").replace("$", "").strip()
        )

        # Calculate expected total
        calculated_total = round(sum_of_items + tax_value, 2)

        # Assertion
        assert calculated_total == displayed_total, (
            f"Price mismatch | Expected: {calculated_total}, "
            f"Displayed: {displayed_total}"
        )

        print(f"Order total verified: ${displayed_total}")

    def finish_order(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
        expect(self.cart_finish_btn).to_be_enabled()
        # action to finish the order
        self.cart_finish_btn.click()
        expect(self.cart_order_complete).to_be_visible()

    def verify_on_checkout_info_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def verify_user_clicked_checkout(self):
        self.cart_checkout_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")