from Tests.base_test import BaseTest
from Resources.users import *
from Pages.home_page import HomePage
from Pages.login_page import LoginPage

class LoginTest(BaseTest):

    def test_login(self):
        #instaniate home page page object
        home = HomePage(self.driver)
        #navigate to login page
        home.nav_to_login()
        #instaniate login page page object
        login = LoginPage(self.driver)
        #login
        login.login(user1_username, user1_password)
        #check if user is logged in
        assert login.read_username() == user1_username.upper()
