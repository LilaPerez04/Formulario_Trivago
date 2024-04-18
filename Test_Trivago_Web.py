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

    def test_calendar_setup(self):
        self.request.set_calendar(Locators.displayed_month_year, data.check_in["month_year_ci"], Locators.next_button, Locators.correct_day,
                                  data.check_in["year_ci"], data.check_in["month_number_ci"], data.check_in["day_ci"])
        self.request.set_calendar(Locators.displayed_month_year, data.check_out["month_year_co"], Locators.next_button, Locators.correct_day,
                                  data.check_out["year_co"], data.check_out["month_number_co"], data.check_out["day_co"])

    def teardown_class(self):
        self.request.driver.quit()
