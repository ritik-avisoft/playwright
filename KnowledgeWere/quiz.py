from playwright.sync_api import Page,expect

def test_quiz(page:Page):
    page.goto("https://www.knowledgeware.in/Automation/")

    expect(page).to_have_title("Elements - Tools Text Box")
    print("Title matched:", page.title())

    page.get_by_role("button", name="Quiz").click()
    page.get_by_text("Example Quiz").click()

    
    expect(page.get_by_text(" Where is Knowledgeware located?? ")).to_have_text(" Where is Knowledgeware located?? ")
    print("q1 found...")

    page.get_by_text("a : Bangalore").click()
    page.get_by_text("c : 2014").click()
    page.get_by_text("d : Quality").click()

    page.locator('id=submit').click()
    correct_ans=page.locator('id=results')
    print(correct_ans.text_content()," from test1") # to print the text inside this obj.

    # page.get_by_role("button", name="Quiz").click()    # this is not working now it's found 2 ele 
    page.wait_for_timeout(2000)
    page.locator('.fa.fa-caret-down').first.click() # clicking the downarrow to expand the quiz buttoon to select the java permitive quiz.
    page.wait_for_timeout(2000)
    page.get_by_text("Java Primitive Quiz").click()

    q1=page.get_by_text(" 1. What is a data type ? ")
    page.wait_for_timeout(2000)
    expect(q1).to_have_text(" 1. What is a data type ? ")
    print("Question:-",q1.text_content())
    page.wait_for_timeout(2000)
    q1Ans=page.get_by_text("d : The collection of variables that a program uses.")
    q1Ans.click()
    page.wait_for_timeout(2000)
    print("you choice:-",q1Ans.text_content())

    q2=page.get_by_text("2. How many bit patterns can a single bit represent?")
    expect(q2).to_have_text("2. How many bit patterns can a single bit represent?")
    print("Question:- " , q2.text_content())
    q2Ans=page.get_by_text("c : 4")
    page.wait_for_timeout(2000)
    q2Ans.click()
    print("you choice:-",q2Ans.text_content())

    page.get_by_role("button", name="Submit Quiz").click()

    ans_of_java=page.locator('id=results')
    print(ans_of_java.text_content()," from 2nd test")


    page.pause()