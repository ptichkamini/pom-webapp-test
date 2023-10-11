from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    #locators - put '*' before to "explode" the tuple into two elements and use in e.g. find element
    USERNAME_ELEMENT = (By.ID, "UsernameOrEmail")
    PASSWORD_ELEMENT = (By.ID, "Password")
    SUBMIT_LOGIN_BUTTON = (By.CLASS_NAME, "btn-login")
    USERNAME_HEADER = (By.ID, "menubar-my-account")

    def input_username(self, username):
        self.find(self.USERNAME_ELEMENT).send_keys(username)

    def input_password(self, password):
        self.find(self.PASSWORD_ELEMENT).send_keys(password)

    def submit_login(self):
        self.find(self.SUBMIT_LOGIN_BUTTON).click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit_login()

    def read_username(self):
        return self.find(self.USERNAME_HEADER).text
