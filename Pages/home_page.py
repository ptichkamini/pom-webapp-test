from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class HomePage(BasePage):
    LOGIN_ELEMENT = (By.ID, "menubar-my-account")
    CART_ELEMENT = (By.ID, "shopbar-cart")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn-action")
    SEARCH_BAR = (By.XPATH, ' //*[@id="header"]/div[2]/div/div/div[1]/div[2]/form/input')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/div[1]/div[2]/form/button/i')

    def nav_to_login(self):
        self.find(self. LOGIN_ELEMENT).click()

    def nav_to_cart(self):
        self.find(self.CART_ELEMENT).click()
        try:
            self.find(self.CHECKOUT_BUTTON).click()

        except NoSuchElementException:
            print("Cart is empty")

    def search_for_item(self, item):
        self.find(self.SEARCH_BAR).send_keys(item)
        self.find(self.SEARCH_BUTTON).click()
