# -*- coding: utf-8 -*-

import HtmlTestRunner
import unittest
from base_test import BaseTest


class SearchTest(BaseTest):

    def setUp(self):
        super(SearchTest, self).setUp()
        self.search_word = "Automation"
        self.search_domain = "siemens.com"
        self.num_of_pages_to_check = 5

    def test_check_first_link_title(self):
        """ Check the first link on search result """
        self.main_page.perform_search(self.search_word)
        self.search_result_page.first_link().click()
        test_check_first_link_title_result = self.search_word in self.driver.title
        self.assertEqual(test_check_first_link_title_result, True,
                         '"{}" is not found in page title "{}"'.format(self.search_word, self.driver.title))

    def test_search_for_expected_domain(self):
        """ The search of expected domain on the first 5 pages of the search result """
        self.main_page.perform_search(self.search_word)
        # get list of links for 1st page
        result_list = self.search_result_page.search_result_links_on_given_pages(self.num_of_pages_to_check)
        test_search_for_expected_domain_result = False
        for domain in result_list:
            if self.search_domain in domain:
                test_search_for_expected_domain_result = True
        self.assertEqual(test_search_for_expected_domain_result, True,
                         'There is no expected domain "{}"'.format(self.search_domain))

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/Brazzard/Desktop/'))
