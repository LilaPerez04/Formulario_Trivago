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
driver.maximize_window()

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

# Establecer la fecha de check in
check_in = {
    "day_ci": '10',
    "month_ci": 'Junio',
    "month_number_ci": '06',
    "year_ci": '2024',
}
# Agregando un nuevo elemento al diccionario check_in (concatenando mes y año)
check_in["month_year_ci"] = check_in["month_ci"] + " " + check_in["year_ci"]

# Establecer la fecha de check out
check_out = {
    "day_co": '10',
    "month_co": 'Julio',
    "month_number_co": '07',
    "year_co": '2024',
}
# Agregando un nuevo elemento al diccionario check_out (concatenando mes y año)
check_out["month_year_co"] = check_out["month_co"] + " " + check_out["year_co"]


# Navegar al mes y año correctos y configurar fecha de check in y check out
def set_calendar(month_year, year, month_number, day):
    while True:
        displayed_month_year = driver.find_element(By.XPATH, '//div[@data-testid="calendar-popover"]//*[contains(@class, "text-center")]//h3[contains(@class, "Heading_heading__xct3h")][1]').text
        if month_year in displayed_month_year:
            break
        else:
            next_button = WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, '//button[@data-testid="calendar-button-next"]')))
            next_button.click()

# Seleccionar el día correcto de check in y check out
    driver.find_element(By.XPATH, f'//button[@data-testid="valid-calendar-day-{year}-{month_number}-{day}"]').click()
    time.sleep(3)


# Llamar a mis parámetros
set_calendar(check_in["month_year_ci"], check_in["year_ci"], check_in["month_number_ci"], check_in["day_ci"])
set_calendar(check_out["month_year_co"], check_out["year_co"], check_out["month_number_co"], check_out["day_co"])
time.sleep(3)


# Seleccionar huespedes
guest_counter_plus = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(
    (By.XPATH, "//button[contains(@data-testid,'guest-selector-apply')]")))
guest_counter_plus.click()
time.sleep(2)


def guest_counter_plus():
    for _ in range(2):
        driver.find_element(guest_counter_plus)
        time.sleep(3)


guest_counter_less = By.XPATH, "//span[contains(@class,'Icon_wrapper__B6IoS Icon_centered__WVTjD Icon_full__sdZ0N')])[2]"


def guest_counter():
    for _ in range(3):
        driver.find_element(guest_counter_less)
        time.sleep(3)


guest_counter_confirm = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(
    (By.XPATH, "//button[@data-testid='guest-selector-apply']")))
guest_counter_confirm.click()
time.sleep(2)


driver.quit()

# Sólo estoy probando el versionamiento
# 2
