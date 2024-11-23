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
        return "PLATE-" + str(random.randrange(1000))

    def detect_vehicle(self):
        self.update_car_park(self._scan_plate())


class EntrySensor(Sensor):

    def __init__(self, id=None, is_active=False, car_park=None):
        super().__init__(id, is_active, car_park)

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected with plate: {plate}")


class ExitSensor(Sensor):

    def __init__(self, id=None, is_active=False, car_park=None):
        super().__init__(id, is_active, car_park)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected with plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)
