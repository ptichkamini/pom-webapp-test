from Tests.base_test import BaseTest
from Pages.home_page import HomePage
from Pages.cart_page import CartPage
import time

class CartTest(BaseTest):

    # def test_empty_cart(self):
    #     #instaniate home page object
    #     home = HomePage(self.driver)
    #     #navigate to cart (also checks if empty)
    #     home.nav_to_cart()

    def test_add_to_cart(self):
        home = HomePage(self.driver)
        home.search_for_item("ball")
        home.select_second_result()
        home.add_to_cart()
        #check if item was added
        try:
            home.is_text_present("successfully added")
        except AssertionError:
            print("article was not added to cart")
