from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    LOGIN_ELEMENT = (By.ID, "menubar-my-account")
    CART_ELEMENT = (By.ID, "shopbar-cart")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn-action")
    SEARCH_BAR = (By.XPATH, ' //*[@id="header"]/div[2]/div/div/div[1]/div[2]/form/input')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/div[1]/div[2]/form/button/i')
    SECOND_ARTICLE = (By.XPATH, "//span[text()='Supreme Golfball']")
        #(By.XPATH, "(//div[@class='artlist artlist-grid artlist-4-cols']//article)[2]")
    ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")

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

    def select_second_result(self):
        self.find(self.SECOND_ARTICLE).click()

    def add_to_cart(self):
        self.find(self.ADD_TO_CART_BUTTON).click()

    def is_text_present(self, text):
        return str(text) in self.driver.page_source
