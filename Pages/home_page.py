from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    LOGIN_ELEMENT = (By.ID, "menubar-my-account")

    def nav_to_login(self):
        self.find(self. LOGIN_ELEMENT).click()