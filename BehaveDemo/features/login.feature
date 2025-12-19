Feature: Login
    @correct-login
    Scenario:verify user login
        Given User on the login page
        When "standard" user enter correct login credentials
        Then User should be on product page

    @all_valid_user_login
    Scenario Outline:Verify valid user login
        Given User on the login page
        When correct credentials entered by "<user_id>"
        Then User should be on product page

        Examples:
            |user_id     |
            |standard    | 
            |problem     | 
            |performance |    



    @incorrect-login
    Scenario:verify incorrect login
        Given User on the login page
        When "standard" user enter valid username and incorrect password
        Then User should see an error message

    @locked-out
    Scenario:verify locked out user login
        Given User on the login page
        When If "locked" user enter correct login credentials
        Then User should see a locked out error message