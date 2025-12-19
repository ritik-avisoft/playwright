from behave import * 
from pages.cart_page import Cart
from pages.product_page import Product
import logging

@given('add "{product}" in the cart')
def add_to_cart(context,product):
    context.add_to_cart_button=Product(context.page)
    context.add_to_cart_button.add_to_cart(product)
    logging.info(f'{product} added successfully in the cart...')

@when('user clicked on cart icon')
def display_cart_list(context):
    context.cart_page=Cart(context.page)
    context.cart_page.open_cart_page()
    logging.info('Now cart page is visible...')

@when('"{product}" should be visible in the cart')
def verifying_specific_product(context,product):
    context.cart_page.product_added_to_cart(product)
    logging.info(f'{product} is verified in the cart...')

@when('products are visible')
def verifying_product(context):
    context.cart_page.verify_cart_product()
    logging.info('All cart product are verified...')

@when('user clicked on checkout')
def click_on_checkout(context):
    context.cart_page.verify_user_clicked_checkout()
    logging.info('Checked-out...')

@then('user remove "{product}" from the cart')
def remove_product_from_cart(context,product):
    context.cart_page.remove_product_from_cart(product)
    logging.info(f'{product} removed from the cart...')


@then('user on checkout information page')
def verify_checkout_info_page(context):
    context.cart_page.verify_on_checkout_info_page()
    logging.info('Now user is on checkout information page...')