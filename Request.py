import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import data

class Request:
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(data.url)
        self.driver.maximize_window()

    def find_hotel(self, locator, value):
        destiny_search = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        destiny_search.click()
        destiny_search.send_keys(value)
        time.sleep(3)

    def calendar_select(self,locator):
        calendar_el = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        calendar_el.click()
        time.sleep(3)
        
