from playwright.sync_api import Page,expect
from utils.crypto_helper import decrypt
from utils.test_data import Test_data as td

class login:
    def __init__(self,page:Page):
        self.page=page
        self.user_name=page.get_by_placeholder("Username")
        self.user_pass=page.get_by_placeholder("Password")
        self.login_submit_btn=page.locator('id=login-button')
        self.login_pg_heading=page.locator('.login_logo')
        self.login_err=page.locator(".error-message-container.error")

    def on_login_page(self):
        self.page.goto("https://www.saucedemo.com/")
        expect(self.page).to_have_url("https://www.saucedemo.com/")

    def logged_in(self,USER, encrypted_password):
        real_password = decrypt(encrypted_password)

        self.page.wait_for_timeout(1000)
        self.user_name.fill(td.USERS[USER])
        self.user_pass.fill(real_password)
        self.login_submit_btn.click()
        self.page.wait_for_timeout(2000)
        return self.page

    def locked_user_login(self,USER,ecrypted_password):
        real_password = decrypt(ecrypted_password)

        self.user_name.fill(td.USERS[USER])
        self.user_pass.fill(real_password)
        self.login_submit_btn.click()
        expect(self.login_err).to_be_visible()

        return self.page
    
    def locked_user_error_message(self):
        expect(self.login_err).to_be_visible()
        expect(self.login_err).to_have_text(td.locked_out_error_message)
        return self.page
    
    def incorrect_login(self,USER):

        self.page.wait_for_timeout(1000)
        self.user_name.fill(td.USERS[USER])
        self.user_pass.fill(td.INCORRECT_PASSWORD_ENCRYPTED)
        self.login_submit_btn.click()
        expect(self.login_err).to_be_visible()

        return self.page
    
    def verify_login_error_message(self):
        expect(self.login_err).to_be_visible()
        expect(self.login_err).to_have_text(td.expected_error_message)