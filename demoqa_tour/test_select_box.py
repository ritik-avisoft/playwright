from playwright.sync_api import Page,expect

def test_select_box(click_elements: Page):

    click_elements.get_by_text("Text Box").click()

    
    click_elements.locator("#userName").fill("Ritik Kr Ranjan")
    click_elements.locator("#userEmail").fill("ritik@mail.com")
    click_elements.locator("#currentAddress").fill("jammu,j&k")
    click_elements.locator("#permanentAddress").fill("patna,Bihar")

    click_elements.locator("#submit").click()
    expect(click_elements.locator("#output")).to_be_visible()
    click_elements.wait_for_timeout(300)