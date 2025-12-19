from behave import *
from pages.cart_page import Cart
from behave.api.pending_step import StepNotImplementedError
import logging

@when('user enter the shipping information')
def enter_shipping_info(context):
    context.fill_details=Cart(context.page) 
    context.fill_details.your_info("Ritik","Ranjan","450054")
    logging.info('Shipping information entered...')

@when('user verify the order details')
def verify_order_overview(context):
    context.fill_details.order_overview()
    logging.info('Order details verified...')

@then('user should be able to place the order')
def place_the_order(context):
    context.fill_details.finish_order()
    logging.info('Order placed successfully...')

