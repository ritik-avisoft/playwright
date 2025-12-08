from playwright.sync_api import Page, expect

def test_click(landingpage: Page):

    # landingpage.get_by_text("Big page with many elements").click()
    bigpage=landingpage.get_by_role("link", name="Big page with many elements")
    bigpage.click()
    print("big Page Opend succesfully")
    landingpage.wait_for_timeout(5000)

    landingpage.locator(".et_pb_button.et_pb_button_0.et_pb_bg_layout_light").click()
    landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(1).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(2).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(3).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(4).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(5).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(6).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(7).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(8).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(9).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(10).click()
    # landingpage.wait_for_timeout(1000)
    # landingpage.locator(".et_pb_button").nth(11).click()
    # landingpage.wait_for_timeout(1000)

    print("Button clicked successfully")
    landingpage.wait_for_timeout(3000)

    twitter=landingpage.locator(".icon.et_pb_with_border").first.click()
    landingpage.wait_for_timeout(3000)


