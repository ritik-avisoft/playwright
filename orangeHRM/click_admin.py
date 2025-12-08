from playwright.sync_api import (Page,expect)

def test_click_admin(login: Page):
    login.get_by_role("link", name="Admin").click()
    print("->> Admin Pannel is Opened Now")
    # login.pause()

    username=login.get_by_role("textbox").nth(1)
    username.fill("Ritik")
    login.pause()               
    # userrole=login.get_by_text("-- Select --").first
    # userrole.click()
    ## get back afte cls of dropdown btn (dynamic)


    login.pause()
