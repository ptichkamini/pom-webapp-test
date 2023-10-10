from Tests.base_test import BaseTest
import time
from selenium.webdriver.common.by import By
from Resources.users import *
from Pages.home_page import HomePage

class LoginTest(BaseTest):

    def test_login(self):
        #instaniate home page page object
        home = HomePage(self.driver)
        home.nav_to_login()
        user_name = self.driver.find_element(By.ID, "UsernameOrEmail")
        user_name.send_keys(user1_login)
        password = self.driver.find_element(By.ID, "Password")
        password.send_keys(user1_passwort)
        submit_login = self.driver.find_element(By.CLASS_NAME, "btn-login")
        submit_login.click()


