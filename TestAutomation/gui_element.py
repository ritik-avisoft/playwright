from playwright.sync_api import Page,expect

def test_enter_details(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_title("Automation Testing Practice")
    print("Title Verified... ")

    #entring name by placeholder 
    
    page.get_by_placeholder("Enter Name").fill("Ritik Kr Ranjan")
    # entring mail by label
    page.get_by_placeholder("Enter EMail").fill("ritikkr@mail.com")
    # entring ph_no by role
    page.get_by_role("textbox", name="Phone").fill("1231231456")

    page.get_by_label("Address:").fill("Patna, Bihar, India ")
    page.get_by_role("radio").first.check() # there are two radio buttons 1st one for male

    page.get_by_label("Monday").check()
    page.get_by_label("Tuesday").check()
    page.get_by_label("Wednenday").check()

    page.pause()

