from playwright.sync_api import Page,expect

# def test_text_box(page:Page):
#     page.goto("https://www.knowledgeware.in/Automation/")

#     expect(page).to_have_title("Elements - Tools Text Box")
#     print("Title matched:", page.title())

#     page.get_by_role("button", name="Elements").click()
#     page.get_by_role("link", name="Text Box").click()

#     page.get_by_placeholder("Full Name").fill("Ritik Kr Ranjan")
#     page.locator('id=mailid').fill("ritikkr@mail.com")
#     page.get_by_placeholder("Current Address").fill("Jammu, J&K, India 180015")
#     page.locator('id=peraddress').fill("Patna, Bihar, India 804401")

#     # page.pause()
#     page.get_by_role("button", name='Submit').click()   #After submitting the op get's disappear within sec....
#     print("test_box Done..")
#     page.pause()

# def test_check_box(page:Page):
#     page.goto("https://www.knowledgeware.in/Automation/check.html#")
#     print("welcome to checkbox page ")

#     page.locator('id=html').check()
#     page.locator('id=css').check()
#     page.locator('id=js').check()
#     page.locator('id=ang').check()
#     page.locator('id=node').check()
#     page.locator('id=dj').check()
#     print("Check Box Done...")
#     page.pause()

# def test_radio_button(page:Page):
#     page.goto("https://www.knowledgeware.in/Automation/radio.html#")

#     page.get_by_role("radio", name="Impressive").check()

#     your_choice=page.locator('id=displayselected')
#     print(your_choice.text_content())


