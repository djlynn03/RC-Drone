import os
import time
import pigpio

class Driver:
    def __init__(self):
        self.ESC_PINS = [4, 17, 27, 22]
        self.max_value = 2000
        self.min_value = 700
        self.start_stop(self.ESC_PINS)
        self.pi = pigpio.pi()

    def set_all(self, val):
        for e in self.ESC_PINS:
            self.pi.set_servo_pulsewidth(e, val)

    def start_stop(self):
        self.set_all(0)

    def calibrate(self):
        self.start_stop()
        print("Disconnect the battery and press Enter")
        inp = input()
        if inp == '':
            self.set_all(self.max_value)
            print("Connect the battery and press Enter")
            inp = input()
            if inp == '':
                self.set_all(self.min_value)
                time.sleep(10)
                self.set_all(0)
                time.sleep(2)
                self.set_all(self.min_value)
                return
        print("Calibration failed")

    def drive(self):
        speed = 1500

driver = Driver()
