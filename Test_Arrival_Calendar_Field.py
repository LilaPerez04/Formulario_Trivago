from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import data
import Locators
from Request import Request


class TestTrivagoWeb:
    request = None

    def setup_class(self):
        self.request = Request()  # Inicializa la clase Request del archivo Request

    def test_fill_hotel_field(self):
        self.request.find_hotel(Locators.destiny_city_searcher, data.hotel)

    def test_arrival_day_no_selected(self):
        self.request.click_on_search_button(Locators.click_on_search_button)
        assert WebDriverWait(self.request.driver, 10).until(
            ec.presence_of_element_located(Locators.search_results))

    def test_clic_calendar_field(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)
        assert self.request.driver.find_element(*Locators.arrival_departure_calendar).is_displayed()

        # Comprueba que el calendario se abre con el mes actual la primera vez

    def test_display_current_month(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)
        current_month_year = WebDriverWait(self.request.driver, 10).until(
            ec.presence_of_element_located(Locators.displayed_month_year)).text
        desired_month_year = data.spanish_months[data.today.month] + " " + str(data.today.year)
        print(f"current month year: {current_month_year}")
        print(f"desired month year: {desired_month_year}")

        assert current_month_year == desired_month_year

    def test_is_today_enabled(self):
        assert self.request.set_calendar(Locators.displayed_month_year, Locators.next_button,
                                         data.today, Locators.today)

    def test_are_future_days_enabled(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)

        assert self.request.set_calendar(Locators.displayed_month_year, Locators.next_button,
                                         data.future, Locators.future)

    def test_are_past_days_disabled(self):
        assert not self.request.set_calendar(Locators.displayed_month_year, Locators.next_button,
                                             data.past, Locators.past)

    def teardown_class(self):
        self.request.driver.quit()
