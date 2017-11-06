# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import *


class SearchText(unittest.TestCase):

    def setUp(self):

        # create FF session
        self.driver = webdriver.Firefox()

        # open page
        self.driver.get("http://www.google.com")
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")

    def search_results(self):

        # find search field
        self.search_field = self.driver.find_element_by_name("q")

        # submit form
        self.search_field.send_keys(search_word)
        self.search_field.submit()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "resultStats"))
        )

    def get_list_of_found_links(self, list_of_links):

        # get the list of found elements
        search_result_list = self.driver.find_elements(By.CSS_SELECTOR, search_result_selectors)

        # create the list of links
        for link in search_result_list:
            list_of_links.append(link.get_attribute('href'))
        return list_of_links

    def test_check_first_link_title(self):

        # find and click first link
        self.search_results()
        self.driver.find_element(By.CSS_SELECTOR, first_link).click()

        # check if page title contains the search word
        assert search_word in self.driver.title
        print '"{}" is found in page title "{}"'.format(search_word, self.driver.title)

    def test_search_for_expected_domain(self):
        result_list = []
        self.search_results()

        # get list of links for 1st page
        list_of_links = self.get_list_of_found_links(list_of_links=[])

        # find other search results pages by data attribute and collect links
        for page_number in range(2, num_of_pages_to_check + 1):
            page_name = 'Page {}'.format(page_number)
            xpath = "//a[contains(@aria-label,'" + page_name + "')]"
            self.driver.find_element(By.XPATH, xpath).click()
            result_list = self.get_list_of_found_links(list_of_links)

        # check if the domain is found
        expected_domain = ""
        for domain in result_list:
            if search_domain in domain:
                expected_domain = domain
        assert search_domain in expected_domain
        print 'There is expected domain "{}"'.format(search_domain)

    def tearDown(self):

        # close the browser
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
