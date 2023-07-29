from hamcrest import assert_that, equal_to
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from modules.main_page.main_page import MainPage
from modules.utils import *


class TestSearchHorizontalMenuAndPagination:

    def setup_class(self):
        self.driver = MainPage.open_page()
        search_class = self.driver.find_element(By.XPATH, SEARCH_CLASS_XPATH_MAIN_PAGE)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, SEARCH_CLASS_XPATH_MAIN_PAGE)))

        search_input = search_class.find_element(By.NAME, SEARCH_NAME_MAIN_PAGE)
        search_input.send_keys("бухгалтерия")
        search_input.send_keys(Keys.ENTER)

    def teardown_class(self):
        MainPage.close_page()

    def test_tcsearch001(self):
        horizontal_menu_elements = self.driver.find_elements(By.XPATH, HORIZONTAL_MENU_ELEMENTS_XPATH)
        first_element_y_coord = horizontal_menu_elements[0].location.get('y')

        for element in horizontal_menu_elements:
            element_y_coord = element.location.get('y')
            assert_that(first_element_y_coord, equal_to(element_y_coord))

    def test_tcsearch002(self):
        search_results_elements = self.driver.find_elements(By.XPATH, SEARCH_RESULT_ELEMENT_XPATH)

        assert_that(len(search_results_elements), equal_to(SEARCH_RESULTS_COUNT_FOR_PAGINATION))
        try:
            element = self.driver.find_element(By.CLASS_NAME, PAGINATION_CLASS_NAME)
            print("Element is present on the page.")
        except NoSuchElementException:
            print("Element is not present on the page.")
            raise
