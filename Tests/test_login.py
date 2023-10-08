from Tests.base_test import BaseTest
import time
from selenium.webdriver.common.by import By

class LoginTest(BaseTest):

    def test_mock(self):
        time.sleep(3)
        login = self.driver.find_element(By.ID, "shopbar-user")
        login.click()
        time.sleep(3)
