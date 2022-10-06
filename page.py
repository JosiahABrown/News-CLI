import locators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def print_us_top(self):
        top_news = locators.MainPageLocators.US_TOP_LATEST
        for i in range(len(top_news)):
            news = self.driver.find_element(
                    *locators.MainPageLocators.US_TOP_LATEST[i])
            print(f'{i}: {news.text}')
