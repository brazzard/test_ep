from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base_page import BasePage


class MainPage(BasePage):

    def search_field(self):
        return self.driver.find_element_by_name("q")

    def perform_search(self, search_word):
        q = self.search_field()
        q.send_keys(search_word)
        q.submit()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "resultStats")))