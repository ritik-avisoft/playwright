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


def test_Xpath(page:Page):
    page.goto("https://www.knowledgeware.in/Automation/web.html")

    salary_elements=page.locator('//tr/td[3]')
    salary_text=salary_elements.all_text_contents()
    print("all salary are now in salary_text....")
    max_sal=0

    for sal in salary_text:
        sal=float(sal)
        if sal>max_sal:
            max_sal=sal
    print("We found the max salary....")
    max_salary_text = f"{max_sal:.2f}"
    print("we convert sal into text again from int")

    page.locator(f"//td[text()='{max_salary_text}']/../td[5]").click()
    print("we clicked on the read more...")
    page.pause()
    
