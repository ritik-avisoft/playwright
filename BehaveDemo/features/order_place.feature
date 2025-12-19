Feature: Order place
    Background: 
        Given User on the login page
        When "standard" user enter correct login credentials
        Then User should be on product page
        
    @order_place
    Scenario: verify order place process
        Given add "bike" in the cart
        And add "tshirt" in the cart
        When user clicked on cart icon
        And products are visible
        And user clicked on checkout
        And user enter the shipping information
        Then user should be able to place the order

