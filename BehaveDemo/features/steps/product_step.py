from behave import *
from pages.login_page import login
from utils.test_data import Test_data as td
import logging

@when('correct credentials entered by "{user_id}"')
def enter_correct_credentials(context,user_id):
    context.login_page=login(context.page)
    context.login_page.logged_in(user_id,td.PASSWORD_ENCRYPTED)
    logging.info(f'{user_id} user logged in successfully...')

