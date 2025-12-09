from playwright.sync_api import Page,expect

def test_quiz(page:Page):
    page.goto("https://www.knowledgeware.in/Automation/")

    expect(page).to_have_title("Elements - Tools Text Box")
    print("Title matched:", page.title())

    # expect(page.locator('h1')).to_have_text("Text Box")
    # print("Heding found:", page.h1())