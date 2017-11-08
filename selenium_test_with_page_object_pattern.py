# -*- coding: utf-8 -*-

import unittest
from page_objects import MainPage, SearchResultsPage
from selenium import webdriver
from config import *


class BaseTest(unittest.TestCase):

    def setUp(self):

        #self.driver = webdriver.Firefox()

        desired_cap = browser_config['ff_44_osx_hs']
        self.driver = webdriver.Remote(
            command_executor='http://' + USERNAME + ':' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

        # open page
        self.driver.get(base_url)
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")

        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultsPage(self.driver)

    def tearDown(self):
        # close the browser
        self.driver.quit()
        pass


class SearchTest(BaseTest):

    def setUp(self):
        super(SearchTest, self).setUp()
        self.search_word = "Automation"
        self.search_domain = "siemens.com"
        self.num_of_pages_to_check = 5

    def test_check_first_link_title(self):
        q = self.main_page.search_field()
        self.main_page.perform_search(q, self.search_word)
        self.search_result_page.first_link().click()
        test_check_first_link_title_result = self.search_word in self.driver.title
        self.assertEqual(test_check_first_link_title_result, True,
                         '"{}" is not found in page title "{}"'.format(self.search_word, self.driver.title))

    def test_search_for_expected_domain(self):
        q = self.main_page.search_field()
        self.main_page.perform_search(q, search_word)
        # get list of links for 1st page
        result_list = self.search_result_page.search_result_links_on_given_pages(self.num_of_pages_to_check)
        test_search_for_expected_domain_result = False
        for domain in result_list:
            if self.search_domain in domain:
                test_search_for_expected_domain_result = True
        self.assertEqual(test_search_for_expected_domain_result, True,
                         'There is no expected domain "{}"'.format(self.search_domain))

if __name__ == '__main__':
    unittest.main()
