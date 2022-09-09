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

    def get_title(self):
        print(self.driver.title)
    # page.MainPage.print_us_top()


if __name__ == '__main__':
    epoch_times = setUp("https://www.theepochtimes.com/us-news")
    print(epoch_times.get_title())
