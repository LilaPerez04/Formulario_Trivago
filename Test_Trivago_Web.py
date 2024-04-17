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
        # To do: Empezar método para seleccionar fechas

    def teardown_class(self):
        self.request.driver.quit()