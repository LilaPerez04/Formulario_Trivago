import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import data
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

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

    def calendar_select(self, locator):
        calendar_el = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        calendar_el.click()
        time.sleep(3)

    # Navegar al mes y año correctos y configurar fecha de check in y check out
    def set_calendar(self, locator, month_year, locator_2, locator_3, year, month_number, day):
        print("Set Calendar")
        print(month_year)
        print(year)
        print(month_number)
        print(day)
        try:
            while True:
                displayed = WebDriverWait(self.driver, 10).until(
                        ec.presence_of_element_located(locator)).text
                print(displayed)
                if month_year in displayed:
                    break
                else:
                    button_next = WebDriverWait(self.driver, 10).until(
                        ec.element_to_be_clickable(locator_2))
                    button_next.click()
        except NoSuchElementException:
            print(f"Error: No se encontró el botón para el día {year}/{month_number}/{day}.")
        except TimeoutException:
            print("Error: Tiempo de espera agotado al esperar que el botón del día sea clickable.")

        # Seleccionar el día correcto de check in y check out
        select_day_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.get_correct_day(locator_3, year, month_number, day)))
        select_day_button.click()
        time.sleep(3)

    def get_correct_day(self, locator, year, month_number, day):
        value = locator[1].format(year=year, month_number=month_number, day=day)
        return (locator[0], value)
