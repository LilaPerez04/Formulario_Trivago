import data
import time
import Locators
from Request import Request
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestTrivagoWeb:
    request = None

    def setup_class(self):
        self.request = Request()  # Inicializa la clase Request del archivo Request

    # Escribe Ocean Coral & Tuequesa en el Campo "hotel"
    def test_fill_hotel_field(self):
        self.request.find_hotel(Locators.destiny_city_searcher, data.hotel)

    # Comprueba que se pueda mandar una solicitud con el calendario de llegada vacío
    #def test_arrival_day_no_selected(self):
    #    self.request.click_on_search_button(Locators.click_on_search_button)
    #    time.sleep(3)
    #    assert self.request.driver.find_element(*Locators.search_results).is_displayed()

    # Da clic en el Campo "calendario"
    def test_clic_calendar_field(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)

    # Comprueba que el calendario aparece al dar clic en el campo
    def test_display_calendar(self):
        assert self.request.driver.find_element(*Locators.arrival_departure_calendar).is_enabled()

    # Comprueba que el calendario se abre con el mes actual la primera vez
    def test_display_current_month(self):
        current_month_year = WebDriverWait(self.request.driver, 10).until(
            ec.presence_of_element_located(Locators.displayed_month_year)).text.lower()
        assert current_month_year == data.check_in["month_year_ci"]

    # Comprueba que solo se puedan elegir fechas apartir del día actual
    def test_day_since_today(self):
        # Prueba día: hoy
        assert self.request.set_calendar(Locators.displayed_month_year, data.check_in["month_year_ci"],
                                         Locators.next_button, Locators.checkin_day)
        time.sleep(3)
        # Prueba día: mañana
        assert self.request.set_calendar(Locators.displayed_month_year, data.check_in_2["month_year_ci_2"],
                                         Locators.next_button, Locators.checkin_day_2)
        time.sleep(3)
        # Prueba día: ayer
        assert not self.request.set_calendar(Locators.displayed_month_year, data.check_in_1["month_year_ci_1"],
                                             Locators.next_button, Locators.checkin_day_1)
        time.sleep(3)

    def teardown_class(self):
        self.request.driver.quit()
