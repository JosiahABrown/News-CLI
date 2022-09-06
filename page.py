import locators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def print_us_top(self):
        top_1 = self.driver.find_element(*locators.MainPageLocators.TOP_1)
        print(top_1.text)
