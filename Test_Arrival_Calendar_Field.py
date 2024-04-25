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

    def test_are_from_now_on_days_enabled(self):
        assert self.request.driver.find_element(*Locators.today).is_enabled()
        assert self.request.driver.find_element(*Locators.future).is_enabled()

    def test_are_past_days_disabled(self):
        assert self.request.driver.find_element(*Locators.past).is_enabled()

    def test_arrival_day_no_selected(self):
        self.request.click_on_search_button(Locators.click_on_search_button)
        time.sleep(3)
        assert self.request.driver.find_element(*Locators.search_results).is_displayed()

    def test_reselect_arrival_date(self):
        self.request.set_calendar(Locators.displayed_month_year, Locators.next_button, data.today, Locators.today)
        self.request.calendar_select(Locators.arrival_departure_calendar)
        self.request.set_calendar(Locators.displayed_month_year, Locators.next_button, data.future, Locators.future)

        assert self.request.is_the_desired_date_selected(Locators.future)

    def teardown_class(self):
        self.request.driver.quit()
#