# Configuramos nuestras librerías
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuramos los drivers para Chrome y especificamos la URL de Trivago
driver = webdriver.Chrome()
driver.get("https://www.trivago.com.mx/es-MX")

# Configuramos la clase

class Trivago:

    #Localizadores

    destiny_city_searcher = (By.CLASS_NAME, 'AutoComplete_searchInput__Km3dQ AutoComplete_inputDropdownContainer__FsmFI')

    destiny_city_text = (By.CLASS_NAME, 'text-m leading-normal font-bold truncate text-grey-900')
    quit_current_destiny = (By.CLASS_NAME, 'Icon_wrapper__B6IoS Icon_s__HT6ei')

    calendar = (By.CLASS_NAME, 'flex items-center 2xl:p-2 2xl:hover:bg-grey-200 2xl:rounded-md group-focus:ring-2 group-focus:ring-blue-700 group-focus:ring-inset')

    #Driver
    def __init__(self, driver):
        self.driver = driver

