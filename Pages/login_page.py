from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Resources.users import *


class LoginPage(BasePage):

    def input_username(self, username):
        username_element = self.driver.find_element(By.ID, "UsernameOrEmail")
        username_element.send_keys(username)

    def input_password(self, password):
        password_element = self.driver.find_element(By.ID, "Password")
        password_element.send_keys(password)

    def submit_login(self):
        submit_login_button = self.driver.find_element(By.CLASS_NAME, "btn-login")
        submit_login_button.click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit_login()