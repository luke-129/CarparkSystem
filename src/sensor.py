from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id=None, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor id: {self.id}, status is: {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return format(random.randrange(1000), "4oig")

    def detect_vehicle(self):
        self._scan_plate()
        self.update_car_park()


class EntrySensor(Sensor):

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Vehicle detected with plate number {plate}")


class ExitSensor(Sensor):

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected with plate number {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)
