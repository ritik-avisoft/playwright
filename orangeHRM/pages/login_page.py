from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.userName_input = page.get_by_role("textbox", name="Username")
        self.userPassword_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def use_login(self, username, password):
        self.userName_input.fill(username)
        self.userPassword_input.fill(password)
        self.login_button.click()

