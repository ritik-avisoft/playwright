from playwright.sync_api import Playwright

def test_add_user(playwright: Playwright):
    api_context=playwright.request.new_context()

    # new_user = {
    #     "name": "Ritik",
    #     "email": "ritik@example.com",
    #     "password": "password123"
    # }
    new_user = {
        "userId": 10,
        "id": 101,
        "title": "Ritik You did your first post api tst ",
        "body": "Kuch nhi bas"
        "copy paste kiya hai lagt hai, "
        "nhi nhi shikh rha hu avi toh help liya hu "
        "gpt se but copy paste nhi "
    }


    response=api_context.post("https://jsonplaceholder.typicode.com/posts",data=new_user)
    # response=api_context.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status==201
    json_data=response.json()
    print(json_data)

    assert json_data["id"]==101

