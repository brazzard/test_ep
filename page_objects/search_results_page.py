from selenium.webdriver.common.by import By
from base_page import BasePage


class SearchResultsPage(BasePage):

    link_selector = "#rso h3 a"

    def first_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.link_selector)

    def page_xpath(self, page_number):
        page_name = 'Page {}'.format(page_number)
        return "//a[contains(@aria-label,'" + page_name + "')]"

    def search_result_links_on_page(self):
        list_of_links = []
        # get the list of found elements
        search_result_selectors_list = self.driver.find_elements(By.CSS_SELECTOR, self.link_selector)

        # create the list of links
        for link in search_result_selectors_list:
            list_of_links.append(link.get_attribute('href'))
        return list_of_links

    def search_result_links_on_given_pages(self, num_of_pages_to_check):
        list_of_links = self.search_result_links_on_page()
        for page_number in range(2, num_of_pages_to_check + 1):
            xpath = self.page_xpath(page_number)
            self.driver.find_element(By.XPATH, xpath).click()
            list_of_links += self.search_result_links_on_page()
        return list_of_links
