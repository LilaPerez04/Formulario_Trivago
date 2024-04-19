import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import Locators
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

    def select_guests_and_rooms(self):
        # Click sobre el boton de habitaciones y huespedes
        self.driver.find_element(Locators.guests_and_rooms_button).click()

    def add_adults(self, locator, adults_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for i in range(adults_to_add):
            self.driver.find_element(*Locators.adults_plus_counter).click()
            time.sleep(1)

    def add_kids(self, kids_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.kids_plus_counter))
        for i in range(kids_to_add):
            self.driver.find_element(*Locators.kids_plus_counter).click()
            time.sleep(1)

    def remove_kids(self, kids_to_remove):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.kids_minus_counter))
        for u in range(kids_to_remove):
            self.driver.find_element(*Locators.kids_minus_counter).click()
            time.sleep(1)

    def add_rooms(self, rooms_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.rooms_plus_counter))
        for i in range(rooms_to_add):
            self.driver.find_element(*Locators.rooms_plus_counter).click()
            time.sleep(1)

    def remove_rooms(self, rooms_to_remove):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.rooms_minus_counter))
        for u in range(rooms_to_remove):
            self.driver.find_element(*Locators.rooms_minus_counter).click()
            time.sleep(1)



    def select_kid1_age(self, age_by_index):

        # Crea un objetos Select
        kid1_age = Select(Locators.kid1_age_dropdown)
        kid1_age.select_by_index(age_by_index)  # Selecciona la primera opcion
        time.sleep(2)

    def select_kid2_age(age):
        kid2_age_dropdown = driver.find_element(By.XPATH, "(//select[contains(@class, 'appearance-none h-10')])[2]")
        kid2_age = Select(kid2_age_dropdown)
        kid2_age.select_by_visible_text(age)  # Selecciona la opcion que contenga el texto 5

    def pets_allowed_checkbox():
        driver.find_element(By.XPATH, "//input[@data-testid='pet-friendly-filter']").click()
        time.sleep(2)

    def restart_guests_view():
        driver.find_element(By.CLASS_NAME, 'FlyoutGuestsRooms_resetBtn__1oUka').click()

    def accept_guests_and_rooms_button():
        driver.find_element(By.XPATH, "//button[text()='Aceptar']").click()

    def click_on_search_button():
        driver.find_element(By.XPATH, "//span[text()='Buscar']").click()

#3345