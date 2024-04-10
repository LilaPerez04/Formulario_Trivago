# Configuración de Librerías:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import requests
from bs4 import BeautifulSoup


# Configuración de los Drivers y URL de Trivago:
driver = webdriver.Chrome()
url = ("https://www.trivago.com.mx/es-MX")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
driver.get(url)



# Interacción con Elementos de la Página:
destiny_city_searcher = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'input-auto-complete')))
destiny_city_searcher.click()
destiny_city_searcher.send_keys("Valentin Imperial Riviera Maya")

arrival_calendar = (By.XPATH, '//button[@data-testid="search-form-calendar-checkin"]')
calendar_right_button = (By.CLASS_NAME, 'absolute right-0')


#button_element = soup.find('button', attrs={'data-testid': 'valid-calendar-day-2024-06-09'}


def pick_a_arrival_date(self, desired_date):
    try:
        # Wait for the delivery date calendar to be clickable
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.arrival_calendar))
        # Click on the delivery date calendar
        self.driver.find_element(*self.arrival_calendar).click()

        click_count = 0
        max_clicks = 12  # Limit up to a year

        while click_count < max_clicks:
            try:
                # Attempt to find the desired calendar element
                month_year_calendar = soup.find('button', attrs={'data-testid': f'valid-calendar-day-{desired_date}'})

                # Usar el XPath para encontrar el elemento deseado


                # If the day element is visible, click on it and exit the loop
                if month_year_calendar.is_displayed():
                    desired_date.click()
                    break
            except NoSuchElementException:
                pass  # Continue looping if the element is not found

            # Click on the "Next" button
            next_button = self.driver.find_element(By.CLASS_NAME, 'next')
            if next_button.is_enabled():
                next_button.click()
                time.sleep(1)
            else:
                print("Next button is not enabled, stopping further navigation.")
                break

        # Search the element with class available and cointains the desired day"
        day_element = self.driver.find_element(By.XPATH,
                                        f"//td[contains(@class, 'available') and text()='{arrival_day}']")
        # clic on day
        day_element.click()
        time.sleep(2)

    except TimeoutException:
        print("Failed to pick a delivery date: Timeout waiting for elements.")
        # Puedes agregar más manejo de errores o lanzar una excepción aquí si es necesario


    def test_select_a_delivery_date(self):
        desired_date = 2024-06-09

        self.enterprise_page.pick_a_delivery_date(arrival_month_year, arrival_day)
        actual_date_value = self.enterprise_page.get_actual_delivery_date()

        # Verificar si la fecha seleccionada es la deseada





time.sleep(3)

#quit_destiny = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.CLASS_NAME, 'Icon_wrapper__B6IoS Icon_s__HT6ei'))))
#quit_destiny.click()

#destiny_city_text = (By.CLASS_NAME, 'text-m leading-normal font-bold truncate text-grey-900')
#time.sleep(3)

driver.quit()

#class Trivago:

    #Localizadores

#    destiny_city_searcher = (By.ID, 'input-auto-complete')
#    destiny_city_text = (By.CLASS_NAME, 'text-m leading-normal font-bold truncate text-grey-900')
#    quit_current_destiny = (By.CLASS_NAME, 'Icon_wrapper__B6IoS Icon_s__HT6ei')



    #Driver
#    def __init__(self, driver):
#        self.driver = driver
