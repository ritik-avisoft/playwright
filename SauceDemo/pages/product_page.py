from playwright.sync_api import Page,expect
from utils.test_data import Test_data as td
import pytest,re

class Product:
    
    def __init__(self,page:Page):
        self.page=page
        self.count=0
        self.Product_title=page.get_by_text("Products")
        #common locators for each product after opening product we will move to saperate one...
        self.back_toProduct=page.locator('id=back-to-products')
        self.inside_product_add_to_cart=page.locator('id=add-to-cart')
        self.inside_product_remove_from_cart=page.locator('id=remove')


        self.sl_backpack_Image=page.get_by_alt_text("Sauce Labs Backpack")
        self.sl_backpack_addToCart=page.locator('id=add-to-cart-sauce-labs-backpack')
        self.sl_backpack_remove=page.locator('id=remove-sauce-labs-backpack') 
        self.sl_backpack_price=self.sl_backpack_addToCart.locator('xpath=preceding-sibling::div')


        self.sl_bike_Image=page.get_by_alt_text("Sauce Labs Bike Light")
        self.sl_bike_addToCart=page.locator('id=add-to-cart-sauce-labs-bike-light')
        self.sl_bike_remove=page.locator('id=remove-sauce-labs-bike-light')
        self.sl_bike_price=self.sl_bike_addToCart.locator('xpath=preceding-sibling::div')


        self.sl_tshirt_Image=page.get_by_alt_text("Sauce Labs Bolt T-Shirt")
        self.sl_tshirt_addToCart=page.locator('id=add-to-cart-sauce-labs-bolt-t-shirt')
        self.sl_tshirt_remove=page.locator('id=remove-sauce-labs-bolt-t-shirt')
        self.sl_tshirt_price=self.sl_tshirt_addToCart.locator('xpath=preceding-sibling::div')
    
        #cart icon loc make sure to assert this 
        self.cart_icon=page.locator(".shopping_cart_link")
        self.cart_icon_for_visual_user=page.locator("id=shopping_cart_container")
        #cartcount locator 
        self.cart_count=page.locator(".shopping_cart_badge")
        #locator to sort product
        self.sort_product=page.locator('.product_sort_container')
        #product Title Name
        self.product_title_name=page.locator(".inventory_item_name ")
        #product img 
        self.product_img=page.locator("img.inventory_item_img")
        #burger button 
        self.burger_menu=page.locator('.bm-burger-button')

    def validate_products_page_loaded(self):
        expect(self.Product_title).to_be_visible()
        # print("You are on Product Page...")

    def add_to_cart(self,product_name:str):
    
        if product_name=="backpack":
            self.sl_backpack_addToCart.click()
        elif product_name=="bike":
            self.sl_bike_addToCart.click()
        elif product_name=="tshirt":
            self.sl_tshirt_addToCart.click()
        else:
            print("Invalid Choice or Product")

    def sort_product_by(self, sort_by: str):
        # Apply sorting
        self.sort_product.select_option(sort_by)

        # Wait for UI to settle , it's also pause the script unitll the ui settled(no req for atleast 500ms)
        self.page.wait_for_load_state("networkidle")

        if sort_by in ["az", "za"]:
            ui_values = self.product_title_name.all_text_contents()
            expected = ui_values.copy()

            if sort_by == "az":
                expected.sort()
            else:
                expected.sort(reverse=True)

        elif sort_by in ["lohi", "hilo"]:
            prices_text = self.page.locator(".inventory_item_price").all_text_contents()

            # Convert "$29.99" → 29.99
            ui_values = [float(p.replace("$", "")) for p in prices_text]
            expected = ui_values.copy()

            if sort_by == "lohi":
                expected.sort()
            else:
                expected.sort(reverse=True)

        else:
            raise ValueError(f"Unsupported sort option: {sort_by}")

        assert ui_values == expected, (
            f"Sorting failed for '{sort_by}'\n"
            f"UI order: {ui_values}\n"
            f"Expected: {expected}"
        )

    def add_product(self, product_name: str):
        self.count += 1
        product = td.PRODUCTS[product_name]
        add_btn = self.page.locator(f"id={product['add_id']}")
        add_btn.click()
        print(f"Clicked add for {product_name}")
        return self.count
    
    def validate_product_count_for_problem_user(self):
        if self.count == 6:
            expect(self.cart_count,"All Add to cart are not enabled !!").to_have_value("6")
        else:
            expect(self.cart_count).to_have_value("3")
    
    def validate_img_for_problem_user(self):
        image_srcs = self.product_img.evaluate_all(
            "imgs => imgs.map(img => img.getAttribute('src'))"
        )
        # Ensure images were actually found
        assert image_srcs, "No product images found on the page"

        # Check all images are identical (known bug)
        unique_images = set(image_srcs)

        assert len(unique_images) == 1, (
            f"Expected all product images to be the same, "
            f"but found {len(unique_images)} different images"
        )
    
    # def compare_price_on_inventort_and_product_price(self,actual_price:str):
    #     self.page.locator(f"")