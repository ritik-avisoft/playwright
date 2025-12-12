from pages.search_box import SearchBox
from playwright.sync_api import Page

def test_search_on_amazon(goto_amazon,page:Page, context):
    # page.goto("https://www.amazon.in/") # not need to do it manually fixture "goto_amazon" handle this 
    search=SearchBox(page)
    search.search("iphone 17 Pro Max 256 GB")

    productPage=search.open_a_product(context)
    product_title = productPage.locator("#productTitle")
    print(product_title)
