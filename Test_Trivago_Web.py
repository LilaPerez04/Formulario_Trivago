# Configuramos nuestras librerías
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# Configuramos los drivers para Chrome y especificamos la URL de Trivago
driver = webdriver.Chrome()
driver.get("https://www.trivago.com.mx/es-MX")

# Vamos a clickear botones para probar localizadores
destiny_city_searcher = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'input-auto-complete')))
destiny_city_searcher.click()
destiny_city_searcher.send_keys("Valentin Imperial Riviera Maya")

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


