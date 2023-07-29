from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.utils import URL_MAIN


class MainPage:
    driver = None

    @classmethod
    def open_page(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(URL_MAIN)
        return cls.driver

    @classmethod
    def close_page(cls):
        cls.driver.quit()

