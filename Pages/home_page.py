from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def nav_to_login(self):
        login = self.driver.find_element(By.ID, "menubar-my-account")
        login.click()

