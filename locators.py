from selenium.webdriver.common.by import By


class MainPageLocators(object):
    # Front page US top news
    x = By.XPATH
    US_TOP_LATEST = [
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[1]/div/a'),
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[2]/div/a'),
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[3]/div/a'),
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[4]/div/a'),
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[5]/div/a'),
            (x, '/html/body/main/div[2]/div[1]/div[2]/div[2]/div[6]/div/a')
            ]
