import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

if __name__ == '__main__':
    pass
