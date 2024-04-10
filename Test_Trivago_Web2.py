# Configuración de Librerías:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

# Configuración de los Drivers y URL de Trivago:
driver = webdriver.Chrome()
url = "https://www.trivago.com.mx/es-MX"
driver.get(url)


# Interacción con Elementos de la Página:

    # Seleccionar destino
destiny_city_searcher = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, 'input-auto-complete')))
destiny_city_searcher.click()
destiny_city_searcher.send_keys("Valentin Imperial Riviera Maya")
time.sleep(3)

    # Seleccionar calendario
arrival_departure_calendar = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//*[@id="__next"]/div[1]/div[2]/section[1]/div[2]/div[4]/div/div[1]/fieldset/button[1])[1]')))
arrival_departure_calendar.click()
time.sleep(3)

# Establecer la fecha que se desea seleccionar
dia = '10'
mes = 'Junio'
mes_numero = '06'
anio = '2024'
mes_anio = mes + ' ' + anio

# Navegar al mes y año correctos
while True:
    displayed_month_year = driver.find_element(By.XPATH, '//div[@data-testid="calendar-popover"]//*[contains(@class, "text-center")]//h3[contains(@class, "Heading_heading__xct3h")][1]').text
    if mes_anio in displayed_month_year:
        break
    else:
        next_button = driver.find_element(By.XPATH, '//button[@data-testid="calendar-button-next"]')
        next_button.click()

# Seleccionar el día correcto
driver.find_element(By.XPATH, f'//button[@data-testid="valid-calendar-day-{anio}-{mes_numero}-{dia}"]').click()
time.sleep(3)

# calendar_right_button = (By.CLASS_NAME, 'absolute right-0')
driver.quit()
