from Tests.base_test import BaseTest
from Pages.home_page import HomePage
from Pages.cart_page import CartPage
import time

class CartTest(BaseTest):

    # def test_empty_cart(self):
    #     #instaniate home page page object
    #     home = HomePage(self.driver)
    #     #navigate to cart (also checks if empty)
    #     home.nav_to_cart()

    def test_add_to_cart(self):
        home = HomePage(self.driver)
        home.search_for_item("ball")
        time.sleep(3)
        #search for a product
        #select it and add it to cart
        #check if item is in the cart



