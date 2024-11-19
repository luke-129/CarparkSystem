class Display:
    def __init__(self, id=None, message="welcome", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.id}: {self.message}"


    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
