from playwright.async_api import Page,expect
import json



def test_my_info(login: Page):
    login.get_by_role("link", name="My Info").click()

    with open("/Users/ritikkumarranjan/Playwright/test_data/personal_details.json") as f:
        data = json.load(f)

    pd=data["personal_details"]
    custom= data["custom_fields"]


    login.get_by_role("textbox", name="First Name").dblclick()
    login.get_by_role("textbox", name="First Name").type(pd["employee_full_name"]["first_name"],delay=200)

    login.get_by_role("textbox", name="Middle Name").dblclick()
    login.get_by_role("textbox", name="Middle Name").type(pd["employee_full_name"]["middle_name"],delay=200)

    login.get_by_role("textbox", name="Last Name").dblclick()
    login.get_by_role("textbox", name="Last Name").type(pd["employee_full_name"]["last_name"],delay=200)

    login.get_by_role("textbox").nth(4).dblclick()
    login.get_by_role("textbox").nth(4).type(pd["employee_id"])
    login.get_by_role("textbox").nth(5).dblclick()
    login.get_by_role("textbox").nth(5).type(pd["other_id"])

    login.locator(".oxd-input.oxd-input--active").nth(5).fill(pd["drivers_license_number"])
    login.get_by_placeholder("yyyy-dd-mm").first.dblclick()
    login.get_by_placeholder("yyyy-dd-mm").first.fill(pd["license_expiry_date"])

    
    login.pause()
    login.wait_for_timeout(5000)



    

'''

    page.locator("div:nth-child(2) > div > .oxd-input-group > div:nth-child(2) > .oxd-input").dblclick()
    page.locator(".oxd-input.oxd-input--focus").fill("4734")
    page.get_by_role("textbox", name="yyyy-dd-mm").first.dblclick()
    page.get_by_role("textbox", name="yyyy-dd-mm").first.fill("2025-10-3847387")

'''
