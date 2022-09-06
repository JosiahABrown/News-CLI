import page
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# service = Service('/usr/bin/chromedriver')
# driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=800,600")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
        )


def epochtimes():
    driver.get("https://www.theepochtimes.com/us-news")
    print(driver.title)
    page.MainPage.print_us_top()


if __name__ == '__main__':
    epochtimes()
