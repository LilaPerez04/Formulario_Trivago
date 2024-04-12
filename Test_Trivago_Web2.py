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

def select_guests_and_rooms():
    #Click sobre el boton de habitaciones y huespedes
    driver.find_element(By.XPATH, "//span[@data-testid='search-form-guest-selector-value']").click()


def add_adults(adults_to_add):
    adults_plus_counter = (By.XPATH, "//button[@data-testid='adults-amount-plus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(adults_plus_counter))
    for i in range(adults_to_add):
        driver.find_element(*adults_plus_counter).click()
        time.sleep(1)


def remove_adults(adults_to_remove):
    adults_minus_counter = (By.XPATH, "//button[@data-testid='adults-amount-minus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(adults_minus_counter))
    for u in range(adults_to_remove):
        driver.find_element(*adults_minus_counter).click()
        time.sleep(1)


def add_kids(kids_to_add):
    adults_plus_counter = (By.XPATH, "//button[@data-testid='children-amount-plus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(adults_plus_counter))
    for i in range(kids_to_add):
        driver.find_element(*adults_plus_counter).click()
        time.sleep(1)


def remove_kids(kids_to_remove):
    kids_minus_counter = (By.XPATH, "//button[@data-testid='children-amount-minus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(kids_minus_counter))
    for u in range(kids_to_remove):
        driver.find_element(*kids_minus_counter).click()
        time.sleep(1)

def add_rooms(rooms_to_add):
    rooms_plus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(rooms_plus_counter))
    for i in range(rooms_to_add):
        driver.find_element(*rooms_plus_counter).click()
        time.sleep(1)


def remove_rooms(rooms_to_remove):

    rooms_minus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-minus-button']//span[1]")
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(rooms_minus_counter))
    for u in range(rooms_to_remove):
        driver.find_element(*rooms_minus_counter).click()
        time.sleep(1)


from selenium.webdriver.support.ui import Select


def select_kid1_age(age_by_index):

    kid1_age_dropdown = driver.find_element(By.XPATH, "//select[contains(@class,'appearance-none h-10')]")
    #Crea un objetos Select
    kid1_age = Select(kid1_age_dropdown)
    kid1_age.select_by_index(age_by_index) #Selecciona la primera opcion
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


def scroll_to_find_hostel_card():
    try:
        hostel_card = driver.find_element(By.XPATH,
                                          "//div[@id='__next']/div[1]/main[1]/div[3]/section[1]"
                                          "/div[1]/div[1]/ol[1]/li[6]/div[1]/article[1]/div[2]/div[1]")

        # Hacer scroll hasta que el elemento sea visible
        driver.execute_script("arguments[0].scrollIntoView(true);", hostel_card)

        # Esperar 2 segundos (puedes ajustar el valor según sea necesario)
        driver.implicitly_wait(2)

    finally:

        driver.quit()


add_adults(4)
remove_adults(2)
add_kids(3)
add_rooms(2)
remove_kids(1)
remove_rooms(1)
select_kid1_age(0)
select_kid2_age("5")
pets_allowed_checkbox()
accept_guests_and_rooms_button()


driver.quit()
# 44
