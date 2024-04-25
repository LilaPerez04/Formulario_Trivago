import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import data
from selenium.common.exceptions import TimeoutException


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

    def get_find_hotel(self, locator):
        return self.driver.find_element(locator).get_property('value')

    def calendar_select(self, locator):
        calendar_el = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        calendar_el.click()
        time.sleep(3)

    def is_calendar_displayed(self, locator):
        return self.driver.find_element(*locator).get_property('value')

    # Navegar al mes y año correctos y configurar fecha de check in y check out

    def set_calendar(self, locator, locator_next_month, day, day_locator):
        try:
            while True:
                # Esperar a que se muestre el mes y año correctos en el calendario
                displayed_month_year = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located(locator)).text

                # Extrae el mes del dia y la primera letra es mayuscula
                month = data.spanish_months[data.today.month]

                # Extrae el año del dia
                year = str(day.year)

                # Formatea el mes y año para buscarlo en el encabezado del calendario
                month_year = f"{month} {year}"

                if month_year in displayed_month_year:
                    break  # Salir del bucle si se muestra el mes y año correctos
                else:
                    # Si el mes y año esperados no están visibles, hacer clic en el botón siguiente
                    button_next = WebDriverWait(self.driver, 10).until(
                        ec.element_to_be_clickable(locator_next_month))
                    button_next.click()

            # Una vez que se muestra el mes y año correctos, seleccionar el día específico
            select_day_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(day_locator))
            select_day_button.click()
            print(f"Día seleccionado correctamente, {day}.")
        except Exception as e:
            print(f"Error en la función set_calendar: {e}")

    def is_this_date_enabled(self, day_locator):
        # Implementación del método aquí
        desired_date_element = self.driver.find_element(*day_locator)
        tabindex = desired_date_element.get_attribute('tabindex')
        return tabindex == "1"

    def is_the_desired_date_selected(self, day_locator):
        # Implementación del método aquí
        desired_date_element = self.driver.find_element(*day_locator)
        desired_date_classes = desired_date_element.get_attribute('class')
        return "bg-blue-800" in desired_date_classes

    def select_guests_and_rooms(self, locator):
        # Click sobre el boton de habitaciones y huespedes
        self.driver.find_element(locator).click()

    def add_adults(self, locator, adults_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for i in range(adults_to_add):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def current_adults_amount(self, locator):
        return self.driver.find_element(*locator).get_property("value")

    def remove_adults(self, locator, adults_to_remove):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for u in range(adults_to_remove):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def add_kids(self, locator, kids_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for i in range(kids_to_add):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def remove_kids(self, locator, kids_to_remove):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for u in range(kids_to_remove):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def current_kids_amount(self, locator):
        return self.driver.find_element(*locator).get_property("value")

    def select_kid_age(self, locator, total_kids, kids_ages):
        for kid_number in range(1, total_kids, +1):
            print(f"El total de niños es: {total_kids}")
            kid_locator = (locator[0], f"{locator[1]}[{kid_number}]")
            print(f"Localizador del niño: {kid_locator}")
            age = kids_ages[kid_number]

            if age is None:
                print(f"No se encontró la edad para el niño {kid_number} en data.kid_num.")
                continue

            print(f"Niño {kid_number} tiene {age} años.")

            try:
                kid_age_element = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located(kid_locator))
                self.scroll_to_find_hostel_card(kid_locator)
                print(kid_age_element.text)
                kid_age = Select(kid_age_element)
                kid_age.select_by_visible_text(age)  # Selecciona la opcion que contenga la edad indicada
                time.sleep(2)

            except TimeoutException:
                print(f"No se encontro el selector de edad para el niño {kid_number}")

    def add_rooms(self, locator, rooms_to_add):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for i in range(rooms_to_add):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def remove_rooms(self, locator, rooms_to_remove):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(locator))
        for u in range(rooms_to_remove):
            self.driver.find_element(*locator).click()
            time.sleep(1)

    def current_rooms_amount(self, locator):
        return self.driver.find_element(*locator).get_property("value")

    def pets_allowed_checkbox(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()
        time.sleep(2)

    def restart_guests_view(self, locator):
        # self.driver.find_element(locator).click()
        restart_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        restart_button.click()
        time.sleep(3)

    def accept_guests_and_rooms_button(self, locator):
        # self.driver.find_element(locator).click()
        accept_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        accept_button.click()
        time.sleep(3)

    def click_on_search_button(self, locator):
        # self.driver.find_element(locator).click()
        search_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        search_button.click()
        time.sleep(3)

    def scroll_to_find_hostel_card(self, locator):
        try:
            # locator[0], locator[1] = locator  # Desempaquetar el localizador
            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((locator[0], locator[1])))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(2)
        finally:
            self.driver.quit()
#