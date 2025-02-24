import pygame
from collections import defaultdict

from Utils.calculations import *

pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[i].init()

clock = pygame.time.Clock()

stick1 = [0, 0] # x,y
stick2 = [0, 0] # up/left is negative, down/right is positive
activationThreshold = 0.05
def handleJoyStickMotion(event):
    if event.axis == 0:
        stick1[0] = event.value
    if event.axis == 1:
        stick1[1] = event.value
    if event.axis == 2:
        stick2[0] = event.value
    if event.axis == 3:
        stick2[1] = event.value
    if (abs(stick1[0]) < activationThreshold > abs(stick1[1])):
        stick1[0] = stick1[1] = 0
    if (abs(stick2[0]) < activationThreshold > abs(stick2[1])):
        stick2[0] = stick2[1] = 0
    print(stick1, stick2, angleDegrees(stick2[0], stick2[1]), magnitude(stick2[0], stick2[1]))

def handleButtonPress(event):
    if event.button == 0:
        print("Button \"A\" Pressed")
    # elif event.button == 1:
    #     print("Button \"B\" Pressed")
    # elif event.button == 2:
    #     print("Button \"X\" Pressed")
    # elif event.button == 3:
    #     print("Button \"Y\" Pressed")
    elif event.button == 4:
        print("Button \"LB\" Pressed")
    elif event.button == 5:
        print("Button \"RB\" Pressed")
    # elif event.button == 6:
    #     print("Button \"Back\" Pressed")
    # elif event.button == 7:
    #     print("Button \"Start\" Pressed")
    # elif event.button == 8:
    #     print("Button \"Left Stick\" Pressed")
    # elif event.button == 9:
    #     print("Button \"Right Stick\" Pressed")
    else:
        print(f"Button {event.button} Pressed")

def skipEvent(event):
    pass

def run():
    eventHandlers = defaultdict(lambda: skipEvent)
    eventHandlers[pygame.JOYAXISMOTION] = handleJoyStickMotion
    eventHandlers[pygame.JOYBUTTONDOWN] = handleButtonPress

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            eventHandlers[event.type](event)