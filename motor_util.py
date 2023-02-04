


def stop(esc):
    for e in esc:
        pi.set_servo_pulsewidth(e, 0)
    