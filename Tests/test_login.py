from Tests.base_test import BaseTest
import time
from selenium.webdriver.common.by import By
from Resources.users import *

class LoginTest(BaseTest):

    def test_mock(self):
        login = self.driver.find_element(By.ID, "menubar-my-account")
        time.sleep(3)
        login.click()
        user_name = self.driver.find_element(By.ID, "UsernameOrEmail")
        user_name.send_keys(user1_login)
        password = self.driver.find_element(By.ID, "Password")
        password.send_keys(user1_passwort)
        submit_login = self.driver.find_element(By.CLASS_NAME, "btn-login")
        submit_login.click()
        search_text = user1_login.upper()
        print(login.text)


