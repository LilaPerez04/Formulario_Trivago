from selenium.webdriver.common.by import By
import data

# Elementos de la página Trivago

# Campo de destino
destiny_city_searcher = (By.ID, 'input-auto-complete')

# Calendario

arrival_departure_calendar = (By.XPATH, "//span[@data-testid='search-form-calendar-checkin-value']")

displayed_month_year = (By.XPATH,
                        '//div[@data-testid="calendar-popover"]//*[contains(@class, "text-center")]'
                        '//h3[contains(@class, "Heading_heading__xct3h")][1]')
next_button = (By.XPATH,
               '//button[@data-testid="calendar-button-next"]')

# Localizadores de los dias de prueba
today = (By.XPATH, f"//time[@datetime='{data.today}']")

yesterday = (By.XPATH, f"//time[@datetime='{data.yesterday}']")

tomorrow = (By.XPATH, f"//time[@datetime='{data.tomorrow}']")

# Menú habitaciones y huéspedes
guests_and_rooms_button = (By.XPATH, "//span[@data-testid='search-form-guest-selector-value']")

# Contadores para agregar y quitar adultos
adults_plus_counter = (By.XPATH, "//button[@data-testid='adults-amount-plus-button']//span[1]")
adults_minus_counter = (By.XPATH, "//button[@data-testid='adults-amount-minus-button']//span[1]")
adults_text_box = (By.XPATH, "//input[@data-testid='adults-amount']")

# Contadores para agregar y quitar niños
kids_plus_counter = (By.XPATH, "//button[@data-testid='children-amount-plus-button']//span[1]")
kids_minus_counter = (By.XPATH, "//button[@data-testid='children-amount-minus-button']//span[1]")
kids_text_box = (By.XPATH, "//input[@data-testid='children-amount']")

 # Dropdowns para escoger las edades de los niños
kid1_age_dropdown = (By.XPATH, "//select[contains(@class, 'appearance-none h-10')]")
kid2_age_dropdown = (By.XPATH, "//select[contains(@class, 'appearance-none h-10')][2]")

# Contadores para agregar y quitar habitaciones
rooms_plus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[1]")
rooms_minus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-minus-button']//span[1]")
rooms_text_box = (By.XPATH, "//input[@data-testid='rooms-amount']")

# Otros bonones dentro de la vista 'Huespedes y Habitaciones'
pets_allowed_checkbox = (By.XPATH, "//input[@data-testid='pet-friendly-filter']")
restart_guests_view_button = (By.CLASS_NAME, 'FlyoutGuestsRooms_resetBtn__1oUka')
accept_guests_and_rooms_button = (By.XPATH, "//button[text()='Aceptar']")

# Botón de buscar
click_on_search_button = (By.XPATH, "//span[text()='Buscar']")

# Vista principal de hoteles encontrados
hostel_card = (By.XPATH, "//div[@id='__next']/div[1]/main[1]/div[3]/section[1]/div[1]/div[1]/ol[1]/li[6]/div[1]"
                         "/article[1]/div[2]/div[1]")
#