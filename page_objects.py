# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def search_field(self):
        return self.driver.find_element_by_name("q")

    def perform_search(self, search_field, search_word):
        search_field.send_keys(search_word)
        search_field.submit()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "resultStats")))


class SearchResultsPage(BasePage):

    def first_link(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > h3 > a")

    def search_result_links_on_page(self):

        list_of_links = []
        # get the list of found elements
        search_result_selectors_list = self.driver.find_elements(By.CSS_SELECTOR, "#rso h3 a")

        # create the list of links
        for link in search_result_selectors_list:
            list_of_links.append(link.get_attribute('href'))
        return list_of_links

    def search_result_links_on_given_pages(self, num_of_pages_to_check):
        list_of_links = self.search_result_links_on_page()
        for page_number in range(2, num_of_pages_to_check + 1):
            page_name = 'Page {}'.format(page_number)
            xpath = "//a[contains(@aria-label,'" + page_name + "')]"
            self.driver.find_element(By.XPATH, xpath).click()
            list_of_links += self.search_result_links_on_page()
        return list_of_links
