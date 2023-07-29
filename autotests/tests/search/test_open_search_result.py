from hamcrest import assert_that, equal_to
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from modules.main_page.main_page import MainPage
from modules.utils import *


class TestSearchOpenSearchResult:

    def setup_class(self):
        self.driver = MainPage.open_page()
        search_class = self.driver.find_element(By.XPATH, SEARCH_CLASS_XPATH_MAIN_PAGE)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, SEARCH_CLASS_XPATH_MAIN_PAGE)))

        search_input = search_class.find_element(By.NAME, SEARCH_NAME_MAIN_PAGE)
        search_input.send_keys("бухгалтерия")
        search_input.send_keys(Keys.ENTER)

    def teardown_method(self):
        self.driver.back()

    def teardown_class(self):
        MainPage.close_page()

    def test_tcsearch003(self):
        first_search_result = self.driver.find_elements(By.XPATH, SEARCH_RESULT_TITLE_CLASS_XPATH)[0]
        first_search_result.click()

        windows_count = len(self.driver.window_handles)
        assert_that(windows_count, equal_to(2))

    def test_tcsearch004(self):
        first_search_result = self.driver.find_elements(By.XPATH, SEARCH_RESULT_TITLE_CLASS_XPATH)[0]
        first_search_result_url = first_search_result.find_element(By.TAG_NAME, "a").get_attribute("href")
        first_search_result.click()

        current_window_handle = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != current_window_handle:
                self.driver.switch_to.window(window_handle)

        current_window_url = self.driver.current_url
        assert_that(first_search_result_url, current_window_url)