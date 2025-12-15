from playwright.sync_api import Page,expect

class Product:
    def __init__(self,page:Page):
        self.page=page
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
        self.sl_tshirt_price=self.sl_tshirt_addToCart.locator('xpath=preceding-sibling::div')
    
        #cart icon loc make sure to assert this 
        self.cart_icon=page.locator(".shopping_cart_link")
        #cartcount locator 
        self.cart_count=page.locator(".shopping_cart_badge")
        #locator to sort product
        self.sort_product=page.locator('.product_sort_container')
        #product Title Name
        self.product_title_name=page.locator(".inventory_item_name ")
    

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
        self.sort_product.select_option(sort_by)

        # UI order
        ui_products = self.product_title_name.all_text_contents()

        # Expected order
        expected_products = ui_products.copy()

        if sort_by == "az":
            expected_products.sort()
        elif sort_by == "za":
            expected_products.sort(reverse=True)
        else:
            raise ValueError(f"Unsupported sort option: {sort_by}")

        assert ui_products == expected_products, (
            f"Sorting failed for '{sort_by}'\n"
            f"UI order: {ui_products}\n"
            f"Expected: {expected_products}"
        )

        print(f"Products sorted correctly by '{sort_by}'")
