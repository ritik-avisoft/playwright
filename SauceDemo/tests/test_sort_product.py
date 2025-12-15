from pages.product_page import Product
from playwright.sync_api import Page,expect

def test_sort_product(test_login_user,page:Page):
    pp=Product(page)
    srt_by=input("enter your sort By choice:- ")
    pp.sort_product_by(srt_by)
    # page.pause()