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

    #    def positive_assert(self, date):
    #        correct_day = self.request.set_calendar(Locators.displayed_month_year, date, Locators.next_button, Locators.checkin_day)
    #        # Comprueba si el código de estado es 201
    #        assert correct_day.status_code == 201

    #    def negative_assert(self, date):
    #        correct_day = self.request.set_calendar(Locators.displayed_month_year, date, Locators.next_button, Locators.checkin_day)
    #        # Comprueba si el código de estado es 400
    #        assert correct_day.status_code == 400
    #        print(correct_day)
    #        print(correct_day.status_code)

    # Comprueba que el calendario aparece al dar clic en el campo

    def test_display_calendar(self):
        assert self.request.driver.find_element(*Locators.checkin_day).is_enabled()

    def teardown_class(self):
        self.request.driver.quit()
