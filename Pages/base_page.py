class BasePage(object):
    def __init__(self, driver, base_url="https://bearstore-testsite.smartbear.com/"):
        self.driver = driver
        self.base_url = base_url

