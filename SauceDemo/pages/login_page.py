from playwright.sync_api import Page,expect
from utils.crypto_helper import decrypt

class login:
    def __init__(self,page:Page):
        self.page=page
        self.user_name=page.get_by_placeholder("Username")
        self.user_pass=page.get_by_placeholder("Password")
        self.login_submit_btn=page.locator('id=login-button')
        self.login_pg_heading=page.locator('.login_logo')
        self.login_err=page.locator(".error-message-container.error")

    def logged_in(self,USER, encrypted_password):
        real_password = decrypt(encrypted_password)

        self.page.wait_for_timeout(1000)
        self.user_name.fill(USER)
        self.user_pass.fill(real_password)
        self.login_submit_btn.click()
        self.page.wait_for_timeout(2000)
        return self.page


