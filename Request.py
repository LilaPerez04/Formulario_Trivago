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

    def set_calendar(self, locator, month_year, locator_next_month, day_button_locator):
        try:
            while True:
                # Esperar a que se muestre el mes y año correctos en el calendario
                displayed_month_year = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(locator)).text

                if month_year in displayed_month_year:
                    break  # Salir del bucle si se muestra el mes y año correctos
                else:
                    # Si el mes y año esperados no están visibles, hacer clic en el botón siguiente
                    button_next = WebDriverWait(self.driver, 10).until(
                        ec.element_to_be_clickable(locator_next_month))
                    button_next.click()

            # Una vez que se muestra el mes y año correctos, seleccionar el día específico
            select_day_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(day_button_locator))
            select_day_button.click()
            print("Día seleccionado correctamente.")
        except Exception as e:
            print(f"Error en la función set_calendar: {e}")

