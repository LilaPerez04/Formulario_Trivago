import time
import data
from Request import Request


class TestFullHappyPath:
    def __init__(self):
        self.request = Request()

    def test_search_a_destiny(self):
        self.request.find_hotel(data.destiny)

    def test_calendar(self):
        self.request.calendar_select()

        # Llamar a mis parámetros
        self.request.set_calendar(data.check_in["month_year_ci"], data.check_in["year_ci"], data.check_in["month_number_ci"], data.check_in["day_ci"])
        self.request.set_calendar(data.check_out["month_year_co"], data.check_out["year_co"], data.check_out["month_number_co"], data.check_out["day_co"])
        time.sleep(3)

    def teardown_class(self):
        self.request.driver.quit()
