# from playwright.sync_api import sync_playwright
import re
from playwright.sync_api import Page, expect
# def test_has_title(page: Page):
#     #page is the tab' which are on browser's
#     page.goto("https://demoqa.com/text-box")
#     #expecting the  action on page should have title in it using re.compile
#     expect(page).to_have_title(re.compile("DEMOQA"))

# def test_to_fill_fullName(page: Page):
#     page.goto("https://demoqa.com/text-box")
#     page.locator("#userName").fill("Ritik Kr Ranjan")
#     expect(page.locator("#userName")).to_have_value("Ritik Kr Ranjan")

# def test_to_fil_userEmail(page: Page):
#     page.goto("https://demoqa.com/text-box")
#     page.locator("#userEmail").fill("example@mail.com")
#     expect(page.locator("#userEmail")).to_have_value("example@mail.com")

# def test_to_fill_currentAddress(page:Page):
#     page.goto("https://demoqa.com/text-box")
#     page.locator("#currentAddress").fill("jammu,jammu,j&k")
#     expect(page.locator("#currentAddress")).to_have_value("jammu,jammu,j&k")

# def test_to_fill_parmanentAddress(page:Page):
#     page.goto("https://demoqa.com/text-box")
#     #inside the locator we use # for id selector
#     page.locator("#permanentAddress").fill("Patna,Bihar")
#     expect(page.locator("#permanentAddress")).to_have_value("Patna,Bihar")

# def test_to_submit_form(page:Page):
#     page.goto("https://demoqa.com/text-box")
#     page.locator("output").click()
#     expect(page.locator("output")).to_be_visible()

# def test_fill_and_submit_form(page: Page):
#     page.goto("https://demoqa.com/text-box")

#     page.locator("#userName").fill("Ritik Kr Ranjan")
#     page.locator("#userEmail").fill("ritik@mail.com")
#     page.locator("#currentAddress").fill("jammu,j&k")
#     page.locator("#permanentAddress").fill("patna,Bihar")

#     #we can use get_by_role also 
#     # page.get_by_role("textbox", name="Full Name").fill("Ritik")
#     # page.get_by_role("textbox", name="Email").fill("ritik@example.com")
#     # page.get_by_role("textbox", name="Current Address").fill("Current Address")
#     # page.get_by_role("textbox", name="Permanent Address").fill("Permanent Address")

#     page.locator("#submit").click()

#     expect(page.locator("#output")).to_be_visible()


# selector 


