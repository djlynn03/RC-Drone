import controller
import os
import time
import pygame
pygame.init()

os.system("sudo pigpiod")
print("initializing pigpio")
time.sleep(2)

controller.run()

'''
left stick- rotate drone
right stick- move drone

left trigger- move down
right trigger- move up

A- take picture


startup sequence to calibrate motors
    if uneven while lifting off, add constant to one motor for rest of session
    lift to a certain height

https://ozeki.hu/p_3002-how-to-setup-a-dc-motor-on-raspberry-pi.html#:~:text=Raspberry%20PI%20DC%20Motor%20code&text=You%20can%20set%20DC%20motor,0%25%20the%20motor%20will%20stop.
'''
