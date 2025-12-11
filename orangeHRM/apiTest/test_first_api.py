from playwright.sync_api import Playwright

def test_get_api(playwright: Playwright):   # Use playwright fixture
    api_context = playwright.request.new_context()

    response = api_context.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status == 200

    json_data = response.json()
    print(json_data)

    assert json_data["id"] == 1

    api_context.dispose()
    print("\nTestCompleted Successfully")
