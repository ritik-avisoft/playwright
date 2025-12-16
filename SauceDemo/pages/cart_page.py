from playwright.sync_api import Page,expect

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
       
        

    def your_info(self, first_name:str, last_name:str, zip:str):
        self.f_name.type(first_name,delay=200)
        self.l_name.type(last_name,delay=200)
        self.zip.type(zip, delay=200)
        # self.continue_button.click()
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

