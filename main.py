import pygame
from calculations import angle
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

keymap = {
    0: "A",
    1: "B",
    2: "X",
    3: "Y",
}

# typemap = {
#     1538: "Hat",
#     1539: "ButtonDown",
#     1540: "ButtonUp",
#     1536: "JoystickMotion"
# }

JoystickMotion = 1536

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

joystick1_pos = [0,0] # x,y
joystick2_pos = [0,0] # up/left is negative, down/right is positive

while keepPlaying:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == JoystickMotion:
            if event.axis == 0:
                joystick1_pos[0] = int(event.value * 100)
            if event.axis == 1:
                joystick1_pos[1] = int(event.value * 100)
            if event.axis == 2:
                joystick2_pos[0] = int(event.value * 100)
            if event.axis == 3:
                joystick2_pos[1] = int(event.value * 100)
            print(joystick1_pos, joystick2_pos, angle(joystick2_pos[0], joystick2_pos[1]))
                
                
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