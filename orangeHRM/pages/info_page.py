from playwright.sync_api import Page

class InfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.info_btm = page.get_by_role("link", name="My Info")
        self.get_f_name = page.get_by_placeholder("First Name")
        self.get_m_name = page.get_by_placeholder("Middle Name")
        self.get_l_name = page.get_by_placeholder("Last Name")

    def get_name(self):
        self.info_btm.click()
        self.page.wait_for_timeout(3000)
        # Wait for inputs to be available
        # self.get_f_name.wait_for(state="visible")

        f = self.get_f_name.input_value()       #earlier i was using text_content() which not work's for input field
        m = self.get_m_name.input_value()
        l = self.get_l_name.input_value()

        print(f"First Name: {f}, Middle Name: {m}, Last Name: {l}")
        return f, m, l
