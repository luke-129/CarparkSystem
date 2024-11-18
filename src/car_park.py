class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"This car park is located at {self.location} and it's capacity is {self.capacity}."

