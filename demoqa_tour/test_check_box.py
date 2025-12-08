from playwright.sync_api import Page, expect

def test_click_check_box(click_elements: Page):
    click_elements.get_by_text("Check Box").click()

    expect(click_elements.get_by_role("heading", name="Check Box")).to_be_visible()
    click_elements.wait_for_timeout(400)

    click_elements.get_by_role("button", name="Toggle").click()
    click_elements.get_by_role("button", name="Toggle").press("Tab")
    # click_elements.get_by_role("button", name="Toggle").press("Spacebar")
    click_elements.wait_for_timeout(5000)
    # click_elements.get_by_role("button", name="Toggle").nth(1).click()
    # click_elements.locator(".rct-node.rct-node-leaf > .rct-text > label > .rct-checkbox > .rct-icon").first.click()
    # click_elements.get_by_role("button", name="Toggle").nth(1).click()
    # click_elements.get_by_role("button", name="Toggle").nth(2).click()
    # click_elements.locator(" .")





    click_elements.wait_for_timeout(1000)










'''    page.goto("https://demoqa.com/checkbox")
    page.get_by_role("button", name="Toggle").click()
    page.get_by_role("button", name="Toggle").nth(1).click()
    page.locator(".rct-node.rct-node-leaf > .rct-text > label > .rct-checkbox > .rct-icon").first.click()
    page.get_by_role("button", name="Toggle").nth(1).click()
    page.get_by_role("button", name="Toggle").nth(2).click()
    page.locator("li:nth-child(2) > ol > li > .rct-text > label > .rct-checkbox > .rct-icon").second.click()
    page.get_by_role("button", name="Toggle").nth(2).click()
    page.get_by_role("button", name="Toggle").nth(3).click()
    page.locator("li:nth-child(3) > ol > li:nth-child(2) > .rct-text > label > .rct-checkbox > .rct-icon").click()
    page.locator(".rct-icon.rct-icon-uncheck").click()
    page.get_by_role("button", name="Toggle").nth(3).click()
    page.get_by_text("You have selected :").click()
    '''