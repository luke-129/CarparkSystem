class Sensor:
    def __init__(self, id=None, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor id: {self.id}, status is: {self.is_active}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass

