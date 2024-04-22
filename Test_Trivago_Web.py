import data
import Locators
from Request import Request


class TestTrivagoWeb:
    request = None

    def setup_class(self):
        self.request = Request()  # Inicializa la clase Request del archivo Request

    def test_search(self):
        self.request.find_hotel(Locators.destiny_city_searcher, data.hotel)
        assert self.request.get_find_hotel(Locators.destiny_city_searcher) == data.hotel

    def test_calendar(self):
        self.request.calendar_select(Locators.arrival_departure_calendar)
        assert self.request.is_calendar_displayed(Locators.displayed_month_year)

    def test_calendar_setup(self):
        self.request.set_calendar(Locators.displayed_month_year, data.check_in["month_year_ci"], Locators.next_button,
                                  Locators.checkin_day)
        self.request.set_calendar(Locators.displayed_month_year, data.check_out["month_year_co"], Locators.next_button,
                                  Locators.checkout_day)

        assert Locators.checkin_day.is_selected()
        assert Locators.checkout_day.is_selected()

    def test_add_adults(self):
        self.request.add_adults(Locators.adults_plus_counter, data.adults_to_add)
        adults_amount = self.request.current_adults_amount(Locators.adults_text_box)
        assert adults_amount == data.total_adults, (f"La cantidad de adultos obtenida es "
                                                    f"{adults_amount} y la esperada {data.total_adults}")

    def test_remove_adults(self):
        self.request.remove_adults(Locators.adults_minus_counter, data.adults_to_remove)
        adults_amount = self.request.current_adults_amount(Locators.adults_text_box)
        assert adults_amount == data.total_adults, (f"La cantidad de adultos obtenida es "
                                                    f"{adults_amount} y la esperada {data.total_adults}")

    def test_add_kids(self):
        self.request.add_kids(Locators.kids_plus_counter, data.kids_to_add)
        kids_amount = self.request.current_kids_amount(Locators.kids_text_box)
        assert kids_amount == data.total_kids, f"La cantidad de niños obtenida es {kids_amount} y la esperada {data.total_kids}"

    def test_remove_kids(self):
        self.request.remove_kids(Locators.kids_minus_counter, data.kids_to_remove)
        kids_amount = self.request.current_kids_amount(Locators.adults_text_box)
        assert kids_amount == data.total_kids, f"La cantidad de niños obtenida es {kids_amount} y la esperada {data.total_kids}"

    def test_add_rooms(self):
        self.request.add_rooms(Locators.rooms_plus_counter, data.rooms_to_add)
        rooms_amount = self.request.current_rooms_amount(Locators.rooms_text_box)
        assert rooms_amount == data.total_kids, f"La cantidad de cuartos obtenida es {rooms_amount} y la esperada {data.total_rooms}"

    def test_remove_rooms(self):
        self.request.remove_rooms(Locators.rooms_minus_counter, data.rooms_to_remove)
        rooms_amount = self.request.current_rooms_amount(Locators.rooms_text_box)
        assert rooms_amount == data.total_kids, f"La cantidad de cuartos obtenida es {rooms_amount} y la esperada {data.total_rooms}"

    def test_select_kids_age(self):
        self.request.select_kid_age(Locators.kid1_age_dropdown, data.kids_ages[1])
        self.request.select_kid_age(Locators.kid2_age_dropdown, data.kids_ages[2])

    def test_pets_allowed_checkbox(self):
        self.request.pets_allowed_checkbox(Locators.pets_allowed_checkbox)

    def test_restart_guests_view(self):
        self.request.restart_guests_view(Locators.restart_guests_view_button)

    def test_accept_guests_and_rooms_button(self):
        self.request.accept_guests_and_rooms_button(Locators.accept_guests_and_rooms_button)

    def test_click_on_search_button(self):
        self.request.click_on_search_button(Locators.click_on_search_button)

    def test_scroll_to_find_hostel_card(self):
        self.request.scroll_to_find_hostel_card(Locators.hostel_card)

    def teardown_class(self):
        self.request.driver.quit()
