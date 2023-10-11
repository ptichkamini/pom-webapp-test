from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver, base_url="https://bearstore-testsite.smartbear.com/"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)