from selenium.webdriver.common.by import By
import data

# Elementos de la página Trivago

# Campo de destino
destiny_city_searcher = (By.ID, 'input-auto-complete')

# Calendario
arrival_departure_calendar = (By.XPATH,
                              '(//*[@id="__next"]/div[1]/div[2]/section[1]/div[2]/div[4]/div/div[1]/fieldset/button[1])'
                              '[1]')
displayed_month_year = (By.XPATH,
                        '//div[@data-testid="calendar-popover"]//*[contains(@class, "text-center")]'
                        '//h3[contains(@class, "Heading_heading__xct3h")][1]')
next_button = (By.XPATH,
               '//button[@data-testid="calendar-button-next"]')
correct_day = (By.XPATH, '//button[@data-testid="valid-calendar-day-{year}-{month_number}-{day}"]')

# Menú habitaciones y huéspedes 
guests_and_rooms_button = (By.XPATH, "//span[@data-testid='search-form-guest-selector-value']")
adults_plus_counter = (By.XPATH, "//button[@data-testid='adults-amount-plus-button']//span[1]")
adults_minus_counter = (By.XPATH, "//button[@data-testid='adults-amount-minus-button']//span[1]")
kids_plus_counter = (By.XPATH, "//button[@data-testid='children-amount-plus-button']//span[1]")
kids_minus_counter = (By.XPATH, "//button[@data-testid='children-amount-minus-button']//span[1]")
rooms_plus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[1]")
rooms_minus_counter = (By.XPATH, "//button[@data-testid='rooms-amount-minus-button']//span[1]")
kid1_age_dropdown = (By.XPATH, "//select[contains(@class,'appearance-none h-10')]")
kid2_age_dropdown = (By.XPATH, "(//select[contains(@class, 'appearance-none h-10')])[2]")
pets_allowed_checkbox = (By.XPATH, "//input[@data-testid='pet-friendly-filter']")
restart_guests_view = (By.CLASS_NAME, 'FlyoutGuestsRooms_resetBtn__1oUka')
accept_guests_and_rooms_button = (By.XPATH, "//button[text()='Aceptar']")
click_on_search_button = (By.XPATH, "//span[text()='Buscar']")
hostel_card = (By.XPATH, "//div[@id='__next']/div[1]/main[1]/div[3]/section[1]/div[1]/div[1]/ol[1]/li[6]/div[1]"
                         "/article[1]/div[2]/div[1]")
