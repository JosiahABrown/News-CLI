import page
from selenium import webdriver


class setUp:

    def __init__(self, website):
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options
                )
        self.website = website
        self.driver.get(website)


class epochTimes(setUp):

    website = "https://www.theepochtimes.com/us-news"

    def __init__(self):
        super().__init__(self.website)

    def get_title(self):
        return self.driver.title

    def us_top(self):
        page.MainPage.print_us_top(self)


if __name__ == '__main__':
    et = epochTimes()
    et.us_top()
