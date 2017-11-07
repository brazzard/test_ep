# -*- coding: utf-8 -*-

import unittest
from page_objects import MainPage, SearchResultsPage
from selenium import webdriver
from config import *


class SearchText(unittest.TestCase):

    def setUp(self):

        # create FF session
        self.driver = webdriver.Firefox()

        # open page
        self.driver.get("http://www.google.com")
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")

        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultsPage(self.driver)

    def tearDown(self):
        # close the browser
        self.driver.quit()
        pass

    def test_check_first_link_title(self):

        q = self.main_page.search_field()
        self.main_page.perform_search(q, search_word)
        self.search_result_page.first_link().click()
        test_check_first_link_title_result = search_word in self.driver.title
        self.assertEqual(test_check_first_link_title_result, True,
                         '"{}" is not found in page title "{}"'.format(search_word, self.driver.title))

    def test_search_for_expected_domain(self):

        q = self.main_page.search_field()
        self.main_page.perform_search(q, search_word)
        # get list of links for 1st page
        result_list = self.search_result_page.search_result_links_on_given_pages(num_of_pages_to_check)
        test_search_for_expected_domain_result = False
        for domain in result_list:
            if search_domain in domain:
                test_search_for_expected_domain_result = True
        self.assertEqual(test_search_for_expected_domain_result, True,
                         'There is no expected domain "{}"'.format(search_domain))

if __name__ == '__main__':
    unittest.main()





