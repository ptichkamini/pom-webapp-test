from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePage(BasePage):
    LOGIN_ELEMENT = (By.ID, "menubar-my-account")
    CART_ELEMENT = (By.ID, "shopbar-cart")
    CHECKOUT_BUTTON =(By.CLASS_NAME, "btn-action")

    def nav_to_login(self):
        self.find(self. LOGIN_ELEMENT).click()

    def nav_to_cart(self):
        self.find(self.CART_ELEMENT).click()
        try:
            self.find(self.CHECKOUT_BUTTON).click()

        except NoSuchElementException:
            print("Cart is empty")


