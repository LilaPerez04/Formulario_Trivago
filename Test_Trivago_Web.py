# Configuración de Librerías:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

import requests
from bs4 import BeautifulSoup

# Configuración de los Drivers y URL de Trivago:
driver = webdriver.Chrome()
url = ("https://www.trivago.com.mx/es-MX")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
driver.get(url)
driver.maximize_window()

# Seleccionar destino
destiny_city_searcher = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'input-auto-complete')))
destiny_city_searcher.click()
destiny_city_searcher.send_keys("Valentin Imperial Riviera Maya")
time.sleep(3)


def pick_checkin_and_checkout_dates_on_calendar(self):

    checkin_date = "2024-05-10"
    checkout_date = "2024-06-12"
    arrival_calendar = (
    By.XPATH, '//*[@id="__next"]/div[1]/div[2]/section[1]/div[2]/div[4]/div/div/fieldset/button[1]/span')

    # Esperar a que el calendario sea clickeable
    WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(arrival_calendar)).click()

    # Establecer un límite para buscar la fecha deseada (hasta un año)
    month_count = 0
    while month_count < 12:

        ########### Fecha de salida ########
        try:
            # Buscar el botón de la fecha deseada dentro del calendario actual
            checkin_date_button = self.driver.find_element(By.XPATH,
                                                   f"//button[@data-testid='valid-calendar-day-{checkin_date}']")

            if checkin_date_button.is_displayed():
                checkin_date_button.click()
                return  # Salir del método una vez que la fecha deseada sea seleccionada
        except:
            pass  # Continuar con el siguiente mes si la fecha no es encontrada

        # Hacer clic en el botón siguiente para avanzar al siguiente mes
        next_button = self.driver.find_element(By.XPATH, "//button[@data-testid='calendar-button-next']")
        next_button.click()
        time.sleep(2)  # Esperar brevemente después de hacer clic en el botón siguiente


        ######### Fecha de regreso ###################
        try:
            # Buscar el botón de la fecha deseada dentro del calendario actual
            checkout_date_button = self.driver.find_element(By.XPATH,
                                                   f"//button[@data-testid='valid-calendar-day-{checkout_date}']")
            checkout_date_button.click()
        except:
            pass  # Continuar con el siguiente mes si la fecha no es encontrada

            # Hacer clic en el botón siguiente para avanzar al siguiente mes
            next_button = self.driver.find_element(By.XPATH, "//button[@data-testid='calendar-button-next']")
            next_button.click()
            time.sleep(1)  # Esperar brevemente después de hacer clic en el botón siguiente

        month_count +=1

#Cierra el driver
driver.quit()


