class Test_data:
    # USERS = [
    #     "standard_user",
    #     "locked_out_user",
    #     "problem_user",
    #     "performance_glitch_user",
    #     "error_user",
    #     "visual_user"
    # ]
    
    USERS = {
    "standard": "standard_user",
    "locked": "locked_out_user",
    "problem": "problem_user",
    "performance": "performance_glitch_user",
    "error": "error_user",
    "visual": "visual_user"
    }

    PASSWORD_ENCRYPTED = "gAAAAABpQ_Xx99B_qFI6oJTyPNjxaaedMHGyhWF92dDl6e0k9NPTP5UtZwNtmKeX_6Ku3aLupZVglScAnedOkrpCQiMewdMKpQ=="

    INCORRECT_PASSWORD_ENCRYPTED= "hfnieuhfiobewalnisnd[cwopfivno sds sdlnpwdfnjpewfcew==!!8764%^&*"

    expected_error_message= " Epic sadface: Username and password do not match any user in this service"

    locked_out_error_message=" Epic sadface: Sorry, this user has been locked out."
    
    PRODUCTS = {
        "backpack": {
            "add_id": "add-to-cart-sauce-labs-backpack",
            "remove_id": "remove-sauce-labs-backpack",
            "price": "$29.99"
        },
        "bike": {
            "add_id": "add-to-cart-sauce-labs-bike-light",
            "remove_id": "remove-sauce-labs-bike-light",
            "price": "$9.99"
        },
        "tshirt": {
            "add_id": "add-to-cart-sauce-labs-bolt-t-shirt",
            "remove_id": "remove-sauce-labs-bolt-t-shirt",
            "price": "$15.99"
        },
        "jacket": {
            "add_id": "add-to-cart-sauce-labs-fleece-jacket",
            "remove_id": "remove-sauce-labs-fleece-jacket",
            "price": "$49.99"
        },
        "onesiet": {
            "add_id": "add-to-cart-sauce-labs-onesie",
            "remove_id": "remove-sauce-labs-onesie",
            "price": "$7.99"
        },
        "tshirt(red)": {
            "add_id": "add-to-cart-test.allthethings()-t-shirt-(red)",
            "remove_id": "remove-test.allthethings()-t-shirt-(red)",
            "price": "$15.99"
        }
    }

