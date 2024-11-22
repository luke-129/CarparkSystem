from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark("moondalup", 100, log_file="moondalup.txt")
entry_sensor = EntrySensor(1, True, car_park)
exit_sensor = ExitSensor(2, True, car_park)
display = Display(1, "Welcome to moondalup", True, car_park)


for x in range(10):
    entry_sensor.detect_vehicle()

exit_sensor.detect_vehicle()
exit_sensor.detect_vehicle()

