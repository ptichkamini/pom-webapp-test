import unittest
from selenium import webdriver
import time


URL = "https://shop.polymer-project.org/"


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)

    def tearDown(self):
        self.driver.quit()

    def test_mock(self):
        driver = self.driver
        driver.get(URL)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
