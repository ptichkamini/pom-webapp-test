import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self, url="https://bearstore-testsite.smartbear.com/"):
        self.driver = webdriver.Chrome()
        self.driver.get(url)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
