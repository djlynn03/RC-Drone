import time
import pigpio

# Electronic Speed Controller constants
MAX_ECS_SPEED = 2000
MIN_ECS_SPEED = 700
ESC_PINS = [4, 17, 27, 22]

class Driver:
    def __init__(self):
        self.Pi = pigpio.pi()

    def _set_all_pins(self, val):
        for pin in ESC_PINS:
            self.Pi.set_servo_pulsewidth(pin, val)

    # Done once at startup
    def calibrate(self):
        self._set_all_pins(0)

        # TODO turn battery off here
        # Pi would output one to a transistor to connect/disconnect the battery
        self._set_all_pins(MAX_ECS_SPEED)

        # TODO turn battery on here
        self._set_all_pins(MIN_ECS_SPEED)
        time.sleep(10)
        self._set_all_pins(0)
        time.sleep(2)
        self._set_all_pins(MIN_ECS_SPEED)

    # Drives pairs of motors together
    def drive(self, val):
        pass

    def hover(self, val):
        pass

driver = Driver()

# Things to work on
# Start up sequence -> drone on, calibrate, hover
# Solder all the components

