import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import Locators
import data


class Request:
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(data.url)
        self.driver.maximize_window()

    def find_hotel(self, destiny):
        destiny_search = WebDriverWait(
            self.driver, 10).until(ec.element_to_be_clickable(Locators.destiny_city_searcher))
        destiny_search.click()
        destiny_search.send_keys(destiny)
        time.sleep(3)

    def calendar_select(self):
        calendar_el = WebDriverWait(
            self.driver, 10).until(ec.element_to_be_clickable(Locators.arrival_departure_calendar))
        calendar_el.click()
        time.sleep(3)

    # Navegar al mes y año correctos y configurar fecha de check in y check out
    def set_calendar(self, month_year, year, month_number, day):
        while True:
            if month_year in self.driver.find_element(Locators.displayed_month_year):
                break
            else:
                next_button = WebDriverWait(self.driver, 10).until(
                    ec.element_to_be_clickable(Locators.next_button))
                next_button.click()

        # Seleccionar el día correcto de check in y check out
        self.driver.find_element(By.XPATH,
                            f'//button[@data-testid="valid-calendar-day-{year}-{month_number}-{day}"]').click()
        time.sleep(3)


def open_guests_and_rooms_view(self):
    # Click sobre el boton de habitaciones y huespedes
    self.driver.find_element(By.XPATH, "//span[@data-testid='search-form-guest-selector-value']").click()


def add_adults(self, adults_to_add):
    adults_plus_counter = (By.XPATH, "//button[@data-testid='adults-amount-plus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(adults_plus_counter))

    for i in range(adults_to_add):  # Haz click sobre el botón '+' un determinado númer de veces
        self.driver.find_element(*adults_plus_counter).click()
        time.sleep(1)


def remove_adults(self, adults_to_remove):
    adults_minus_counter = (By.XPATH, "//button[@data-testid='adults-amount-minus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(adults_minus_counter))

    for u in range(adults_to_remove): # Haz click sobre el botón '-' un determinado número deveces
        self.driver.find_element(*adults_minus_counter).click()
        time.sleep(1)


def add_kids(self, kids_to_add):
    kids_plus_counter = (By.XPATH, "//button[@data-testid='children-amount-plus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(kids_plus_counter))

    for i in range(kids_to_add): # Haz click sobre el botón '+' un determinado númer de veces
        self.driver.find_element(*kids_plus_counter).click()
        time.sleep(1)


def remove_kids(self, kids_to_remove):
    kids_minus_counter = (By.XPATH, "//button[@data-testid='children-amount-minus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(kids_minus_counter))

    for u in range(kids_to_remove): # Haz click sobre el botón '-' un determinado número deveces
        self.driver.find_element(*kids_minus_counter).click()
        time.sleep(1)


def add_rooms(self, rooms_to_add):
    rooms_plus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(rooms_plus_counter))

    for i in range(rooms_to_add): # Haz click sobre el botón '+' un determinado númer de veces
        self.driver.find_element(*rooms_plus_counter).click()
        time.sleep(1)


def remove_rooms(self, rooms_to_remove):
    rooms_minus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-minus-button']//span[1]")
    WebDriverWait(self.driver, 10).until(
        ec.element_to_be_clickable(rooms_minus_counter))

    for u in range(rooms_to_remove): # Haz click sobre el botón '-' un determinado número deveces
        self.driver.find_element(*rooms_minus_counter).click()
        time.sleep(1)


def select_kid1_age(self, age_by_index):

    kid1_age_dropdown = self.driver.find_element(By.XPATH, "//select[contains(@class,'appearance-none h-10')]")
    # Crea un objetos Select
    kid1_age = Select(kid1_age_dropdown)
    kid1_age.select_by_index(age_by_index)  # Selecciona la primera opcion
    time.sleep(2)


def select_kid2_age(self, age):
    kid2_age_dropdown = self.driver.find_element(By.XPATH, "(//select[contains(@class, 'appearance-none h-10')])[2]")
    kid2_age = Select(kid2_age_dropdown)
    kid2_age.select_by_visible_text(age)  # Selecciona la opcion que contenga el texto 5


def pets_allowed_checkbox(self):
    # Haz click sobre la checkbox de 'se permiten mascotas'
    self.driver.find_element(By.XPATH, "//input[@data-testid='pet-friendly-filter']").click()
    time.sleep(2)


def restart_guests_view(self):
    self.driver.find_element(By.CLASS_NAME, 'FlyoutGuestsRooms_resetBtn__1oUka').click()


def accept_guests_and_rooms_button(self):
    self.driver.find_element(By.XPATH, "//button[text()='Aceptar']").click()


def click_on_search_button(self):
    self.driver.find_element(By.XPATH, "//span[text()='Buscar']").click()


def scroll_to_find_hostel_card(self):
    try:
        hostel_card = self.driver.find_element(By.XPATH,
                                          "//div[@id='__next']/div[1]/main[1]/div[3]/section[1]"
                                          "/div[1]/div[1]/ol[1]/li[6]/div[1]/article[1]/div[2]/div[1]")

        # Hacer scroll hasta que el elemento sea visible
        self.driver.execute_script("arguments[0].scrollIntoView(true);", hostel_card)

        # Esperar 2 segundos (puedes ajustar el valor según sea necesario)
        self.driver.implicitly_wait(2)

    finally:

        self.driver.quit()
        
