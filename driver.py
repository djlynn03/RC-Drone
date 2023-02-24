import time
import pigpio

from Utils.calculations import *
from copy import deepcopy

# Electronic Speed Controller constants
MAX_ECS_SPEED = 2000
MIN_ECS_SPEED = 700
EQUILIBRIUM_SPEED = "IMPLEMENT ME"
# Front left - 4
# Front right - 17
# Back left - 22
# Back right - 27
ESC_PINS = [4, 17, 27, 22]


class Driver:
    def __init__(self):
        self.Pi = pigpio.pi()
        # Front left, front right, back left, back right
        self.motorSpeeds = [MIN_ECS_SPEED] * 4
        self.isRotating = False
        self.isMoving = False
        self.currentDirection = "None"

    def boundSpeed(self, speed):
        return max(min(speed, MAX_ECS_SPEED), MIN_ECS_SPEED)

    def setAllMotors(self, speed):
        self.motorSpeeds = [self.boundSpeed(speed)] * 4
        for pin, speed in zip(ESC_PINS, self.motorSpeeds):
            self.Pi.set_servo_pulsewidth(pin, speed)

    def killMotors(self):
        self.setAllMotors(MIN_ECS_SPEED)

    def setRightDiagonal(self, speed):
        # Sets front right and back left motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[1], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[2], self.boundSpeed(speed))

    def setLeftDiagonal(self, speed):
        # Sets front left and back right motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[0], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[3], self.boundSpeed(speed))

    def setFrontMotors(self, speed):
        # Sets front left and front right motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[0], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[1], self.boundSpeed(speed))

    def setBackMotors(self, speed):
        # Sets back left and back right motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[2], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[3], self.boundSpeed(speed))

    def setLeftMotors(self, speed):
        # Sets front left and back left motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[0], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[2], self.boundSpeed(speed))

    def setRightMotors(self, speed):
        # Sets front right and back right motors
        self.Pi.set_servo_pulsewidth(ESC_PINS[1], self.boundSpeed(speed))
        self.Pi.set_servo_pulsewidth(ESC_PINS[3], self.boundSpeed(speed))

    # Done once at startup
    def calibrate(self):
        self.setAllMotors(0)

        # TODO turn battery off here
        # Pi would output one to a transistor to connect/disconnect the battery
        input("disconnect battery and press enter")
        self.setAllMotors(MAX_ECS_SPEED)
        time.sleep(1)
        input("connect battery and press enter")
        # TODO turn battery on here
        self.setAllMotors(MIN_ECS_SPEED)
        time.sleep(10)
        self.setAllMotors(0)
        time.sleep(2)
        self.setAllMotors(MIN_ECS_SPEED)

    # Drives pairs of motors together
    def manual_drive(self):
        self.setAllMotors(self.motorSpeeds[0])
        inp = input("a - decrease, d - increase, q - decrease a lot, e - increase a lot")
        if inp == "q":
            self.setAllMotors(self.motorSpeeds[0] - 100)
        elif inp == "e":
            self.setAllMotors(self.motorSpeeds[0] + 100)
        elif inp == "d":
            self.setAllMotors(self.motorSpeeds[0] + 10)
        elif inp == "a":
            self.setAllMotors(self.motorSpeeds[0] - 10)
        if inp:
            print(f"speeds = {self.motorSpeed}")

    def hover(self):
        self.setAllMotors(EQUILIBRIUM_SPEED)
        self.isRotating = False
        self.isMoving = False

    def ascend(self):
        self.setAllMotors(EQUILIBRIUM_SPEED + 10)

    def descend(self):
        self.setAllMotors(EQUILIBRIUM_SPEED - 10)

    def rotate(self, leftStickX, leftStickY):
        if leftStickX == leftStickY == 0:
            self.isRotating = False
            self.setAllMotors(EQUILIBRIUM_SPEED)
        elif not self.isMoving:
            if not self.isRotating:
                self.isRotating = True
                angle = angleDegrees(leftStickX, leftStickY)
                if angle < 90 or angle > 270:
                    # Turn right
                    self.setLeftDiagonal(EQUILIBRIUM_SPEED + 10)
                else:
                    # Turn left
                    self.setRightDiagonal(EQUILIBRIUM_SPEED + 10)

    def move(self, rightStickX, rightStickY):
        if rightStickX == rightStickY == 0:
            self.isMoving = False
            self.currentDirection = "None"
            self.setAllMotors(EQUILIBRIUM_SPEED)
        elif not self.isRotating:
            if not self.isMoving:
                self.isMoving = True
                angle = angleDegrees(rightStickX, rightStickY)
                if angle > 45 and angle < 135:
                    # Move forward
                    if self.currentDirection != "Forward":
                        self.setAllMotors(EQUILIBRIUM_SPEED)
                        self.currentDirection = "Forward"
                    self.setBackMotors(EQUILIBRIUM_SPEED + 10)
                elif angle > 225 and angle < 315:
                    # Move backward
                    if self.currentDirection != "Backward":
                        self.setAllMotors(EQUILIBRIUM_SPEED)
                        self.currentDirection = "Backward"
                    self.setFrontMotors(EQUILIBRIUM_SPEED + 10)
                elif angle > 135 and angle < 225:
                    # Move left
                    if self.currentDirection != "Left":
                        self.setAllMotors(EQUILIBRIUM_SPEED)
                        self.currentDirection = "Left"
                    self.setRightMotors(EQUILIBRIUM_SPEED + 10)
                else:
                    # Move right
                    if self.currentDirection != "Right":
                        self.setAllMotors(EQUILIBRIUM_SPEED)
                        self.currentDirection = "Right"
                    self.setLeftMotors(EQUILIBRIUM_SPEED + 10)

# Things to work on
# Start up sequence -> drone on, calibrate, hover
# Solder all the components
if __name__ == "__main__":
    d = Driver()
    d.calibrate()
