from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from p6_POM_DBB_Page_Object_Model_Behaviour_Driven_Development.Curs12_POM_BDD.browser import Browser
from unittest import TestCase as Assert


class BasePage(Browser):
    BASE_URL = "https://demo.nopcommerce.com/"

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    def verify_url(self, expected_url):
        Assert.assertEquals(self.driver.current_url, expected_url, "URLs are not matching")