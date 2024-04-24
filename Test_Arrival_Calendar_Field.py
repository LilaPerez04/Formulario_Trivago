import time

import data
import Locators
from Request import Request


class TestTrivagoWeb:
    request = None

    def setup_class(self):
        self.request = Request()  # Inicializa la clase Request del archivo Request

    def test_search(self):
        self.request.find_hotel(Locators.destiny_city_searcher, data.hotel)

    def test_calendar(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)

    def test_display_calendar(self):
        assert self.request.driver.find_element(*Locators.tomorrow).is_enabled()

    def test_reselect_arrival_date(self):
        self.request.set_calendar(Locators.displayed_month_year, Locators.next_button, Locators.tomorrow)
        time.sleep(2)
        self.request.calendar_select(Locators.arrival_departure_calendar)
        time.sleep(2)
        self.request.set_calendar(Locators.displayed_month_year, Locators.next_button, Locators.today)
        time.sleep(2)
        assert self.request.driver.find_element(*Locators.today).is_selected()

    def teardown_class(self):
        self.request.driver.quit()
#