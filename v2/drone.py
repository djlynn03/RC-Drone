import time
import pigpio

# Electronic Speed Controller constants
MAX_ECS_SPEED = 2000
MIN_ECS_SPEED = 700
ESC_PINS = [4, 17, 27, 22]  # fl, fr, br, bl
EQUILIBRIUM_SPEED = 760


class Driver:
    def __init__(self):
        self.Pi = pigpio.pi()

        self.speeds = [MIN_ECS_SPEED, MIN_ECS_SPEED,
                       MIN_ECS_SPEED, MIN_ECS_SPEED] # 4,17,27,22

    def set_all_motors(self, val):
        self.set_fl_motor(val)
        self.set_fr_motor(val)
        self.set_br_motor(val)
        self.set_bl_motor(val)
    
    def set_each_motor(self, arr):
        for p, s in zip(ESC_PINS, arr):
            self.Pi.set_servo_pulsewidth(p, s)

    def set_fl_motor(self, val):  # front left motor
        self.Pi.set_servo_pulsewidth(4, val)

    def set_fr_motor(self, val):  # front right motor
        self.Pi.set_servo_pulsewidth(17, val)

    def set_br_motor(self, val):  # back right motor
        self.Pi.set_servo_pulsewidth(27, val)

    def set_bl_motor(self, val):  # back left motor
        self.Pi.set_servo_pulsewidth(22, val)

    # Done once at startup
    def calibrate(self):
        print("Calibrating")
        self.set_all_motors(0)

        # TODO turn battery off here
        # Pi would output one to a transistor to connect/disconnect the battery
        input("Disconnect the battery and press enter")
        self.set_all_motors(MAX_ECS_SPEED)
        time.sleep(1)
        input("Connect the battery and press enter")
        # TODO turn battery on here
        self.set_all_motors(MIN_ECS_SPEED)
        time.sleep(4)
        self.set_all_motors(0)
        time.sleep(2)

        print("Done calibrating")
        self.set_all_motors(MIN_ECS_SPEED)
        

    def bound_speed(self, val):
        return max(min(val, MAX_ECS_SPEED), MIN_ECS_SPEED)

    def move_up(self):
        self.speeds = [self.bound_speed(i + 10) for i in self.speeds]
        self.set_each_motor(self.speeds)
        # Drives pairs of motors together

    def hover(self):
        self.speeds = [EQUILIBRIUM_SPEED for _ in self.speeds]


if __name__ == "__main__":
    driver = Driver()
    driver.calibrate()

# Things to work on
# Start up sequence -> drone on, calibrate, hover
# Solder all the components
