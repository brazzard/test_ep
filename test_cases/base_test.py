# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from config import *
from page_objects.main_page import MainPage
from page_objects.search_results_page import SearchResultsPage


class BaseTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox(executable_path=geckodriver_path)

        # desired_cap = browser_config['ff_44_osx_hs']
        # self.driver = webdriver.Remote(
        #     command_executor='http://' + USERNAME + ':' + ACCESS_KEY + '@hub.browserstack.com:80/wd/hub',
        #     desired_capabilities=desired_cap)

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



