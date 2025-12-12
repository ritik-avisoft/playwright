from playwright.sync_api import Page,expect


class SearchBox:
    def __init__(self, page:Page):
        self.page=page
        self.search_box=page.locator('id=twotabsearchtextbox')

    def search(self, searchKeyword:str):
        self.search_box.fill(searchKeyword)
        self.search_box.press("Enter")
        self.page.wait_for_timeout(3000)
    
    def open_a_product(self, context):
        with context.expect_page() as new_page_info:
            self.page.locator("div[data-cel-widget='search_result_0'] a").click()
        return new_page_info.value

