class BasePage(object):
    def __init__(self, driver, base_url="https://shop.polymer-project.org/"):
        self.driver = driver
        self.base_url = base_url
