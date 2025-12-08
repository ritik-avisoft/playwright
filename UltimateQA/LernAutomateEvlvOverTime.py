from playwright.sync_api import Page,expect
import re

def test_click_the_link(landingpage: Page):
    landingpage.get_by_text("Learn how to automate an application that evolves over time").click()
    print("Sample Application Started ")

    print("Check that we are on sprint 1")
    # expect(landingpage.get_by_role("heading", )).to_contain_text("Sprint 1")
    expect(landingpage.locator("h1")).to_contain_text("Sprint 1")
    print("Good to go with Sprint-1")
    # landingpage.pause()
    # landingpage.get_by_text("firstname").fill("Ritik")   # get by text is not ment  to find the input box
    # landingpage.get_by_label("First name:").fill("Ritik")  # still not working
    landingpage.get_by_role("textbox").fill("Ritik")
    landingpage.wait_for_timeout(3000)
    landingpage.get_by_role("link", name="Go to the next sprint").click()

    print("Check that we are on sprint 2")
    expect(landingpage.locator("h1")).to_contain_text("Sprint 2")
    print("Welcome to Sprint 3")
    landingpage.locator("input[name=\"firstname\"]").fill("Ritik")
    landingpage.locator("input[name=\"lastname\"]").fill("Ranjan")
    landingpage.wait_for_timeout(3000)
    print("Sprint 2 Completed")

    landingpage.get_by_role("link", name="Go to sprint 3").click()
    landingpage.wait_for_timeout(2000)

    print("Check that we are on sprint 3")    
    expect(landingpage.locator("h1")).to_contain_text("Sprint 3")
    print("Welcome to Sprint 3")
    # landingpage.locator("input[name='gender'][value='male']").check()
    # landingpage.get_by_label("First name").fill("Riya")   #both are not working coz the lable is not connected 
    # landingpage.get_by_label("Last name").fill("Ranjan")
    landingpage.get_by_role("textbox").first.type("Riya")
    landingpage.get_by_role("textbox").nth(1).type("Ranjan")
    landingpage.wait_for_timeout(3000)
    landingpage.get_by_role("link", name="Go to sprint 4").click()
    print("Sprint 3 Completed")

