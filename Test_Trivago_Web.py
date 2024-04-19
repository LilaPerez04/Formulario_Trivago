import data
import Locators
from Request import Request
import time


class TestTrivagoWeb:
    request = None

    def setup_class(self):
        self.request = Request()  # Inicializa la clase Request del archivo Request

    def test_search(self):
        self.request.find_hotel(Locators.destiny_city_searcher, data.hotel)

    def test_calendar(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)

    def test_calendar_setup(self):
        self.request.set_calendar(Locators.displayed_month_year, data.check_in["month_year_ci"], Locators.next_button,
                                  Locators.checkin_day)
        self.request.set_calendar(Locators.displayed_month_year, data.check_out["month_year_co"], Locators.next_button,
                                  Locators.checkout_day)
        time.sleep(3)

    def test_add_adults(self):
        self.request.add_adults(Locators.adults_plus_counter, )

    def teardown_class(self):
        self.request.driver.quit()
        
