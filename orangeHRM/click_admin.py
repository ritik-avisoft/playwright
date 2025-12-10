from playwright.sync_api import (Page,expect)

def test_click_admin(login: Page):
    login.get_by_role("link", name="Admin").click()
    # login.pause()
    login.get_by_text("Leave").click()
    login.get_by_role("link", name="Apply").click()
    login.get_by_text("-- Select --").click()
    login.get_by_text("CAN - Bereavement").click()
    Leave_Balance=login.locator(".oxd-text.oxd-text--p.orangehrm-leave-balance-text").text_content()
    print(Leave_Balance)

    login.get_by_placeholder("yyyy-dd-mm").nth(0).fill("2025-12-11")
    # login.get_by_placeholder("yyyy-dd-mm").nth(1).fill("2025-22-12")   # filling twice..
    login.get_by_role("textbox", name="yyyy-dd-mm").nth(1).clear()
    login.pause()
    
    login.locator("textarea").click()
    login.locator("textarea").fill("testing for apply leave")

    login.get_by_role("button", name="Apply").click()
    login.wait_for_timeout(5000)




