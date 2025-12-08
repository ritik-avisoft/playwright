from playwright.sync_api import Page, expect

def test_click_check_box(click_elements: Page):
    click_elements.get_by_text("Radio Button").click()

    radio_yes=click_elements.locator(' xpath=//input[@id="yesRadio"]')
    
    # radio_yes.click()
    # click_elements.wait_for_timeout(3000)

    click_elements.pause()