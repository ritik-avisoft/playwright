Feature: Cart Process

    Background: 
        Given User on the login page
        When "standard" user enter correct login credentials
        Then User should be on product page

    @add_to_cart
    Scenario Outline: verify add item to cart
        Given add "<Product_name>" in the cart
        When user clicked on cart icon
        And "<Product_name>" should be visible in the cart
        
        Examples:
            |Product_name   |
            |bike           | 
            |backpack       | 
            |tshirt         |

    @remove_from_cart
    Scenario: verify remove item from cart
        Given add "bike" in the cart
        And add "tshirt" in the cart
        When user clicked on cart icon
        And products are visible
        Then user remove "bike" from the cart

    @checkout
    Scenario: verify checkout process
        Given add "bike" in the cart
        And add "tshirt" in the cart
        When user clicked on cart icon
        And products are visible
        When user clicked on checkout
        Then user on checkout information page
