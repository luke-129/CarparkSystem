from sensor import ExitSensor, EntrySensor, Sensor
from car_park import CarPark
import unittest


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark()
        self.car_park_2 = CarPark()
        self.exit_sensor = ExitSensor(1, False, self.car_park)
        self.entry_sensor = EntrySensor(2, False, self.car_park_2)

    def test_sensor_initialized_attributes(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 2)
        self.assertEqual(self.exit_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, False)
        self.assertEqual(self.entry_sensor.is_active, False)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)


    def test_detect_vehicle_method(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
        self.assertTrue(len(self.car_park.plates) == 0)
        self.assertTrue(len(self.car_park_2.plates) == 0)