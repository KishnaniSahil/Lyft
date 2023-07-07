import unittest
from datetime import datetime
from engine.model.battery import SpindlerBattery, NubbinBattery
from engine.model.engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service_when_due(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service_when_not_due(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service_when_due(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service_when_not_due(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service_when_due(self):
        last_service_date = datetime.today().date()
        current_mileage = 35000
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_does_not_need_service_when_not_due(self):
        last_service_date = datetime.today().date()
        current_mileage = 45000
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service_when_warning_light_on(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_does_not_need_service_when_warning_light_off(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service_when_due(self):
        last_service_date = datetime.today().date()
        current_mileage = 70000
        last_service_mileage = 50000
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_does_not_need_service_when_not_due(self):
        last_service_date = datetime.today().date()
        current_mileage = 80000
        last_service_mileage = 50000
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
