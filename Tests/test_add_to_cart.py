from Tests.base_test import BaseTest
from Pages.home_page import HomePage
from Pages.cart_page import CartPage

class LoginTest(BaseTest):

    def test_empty_cart(self):
        #instaniate home page page object
        home = HomePage(self.driver)
        #navigate to cart
        home.nav_to_cart()

    def test_add_to_cart(self):
        pass

