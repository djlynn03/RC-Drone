from inputs import get_gamepad
from drone import Driver

def event_loop():
    driver = Driver()
    driver.calibrate()
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)

            # joystick values range from -2^8 to 2^8-1
            if event.code == "ABS_RX": # right stick l/r
                pass
            elif event.code == "ABS_RY": # right stick u/d
                pass
            elif event.code == "ABS_X": # right stick l/r
                pass
            elif event.code == "ABS_Y": # right stick u/d
                pass

            # trigger values range from 0-1023
            elif event.code == "ABS_RZ": # right trigger
                driver.move_up()
                pass

            elif event.code == "ABS_Z": # left trigger
                pass
            elif event.code == "BTN_WEST" and event.state == 1: # Y button down
                pass
            elif event.code == "BTN_NORTH" and event.state == 1: # X button down
                pass
            elif event.code == "BTN_SOUTH" and event.state == 1: # A button down
                pass
            elif event.code == "BTN_EAST" and event.state == 1: # B button down
                pass
