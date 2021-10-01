from time import sleep
import winsound


def focus(m=45, r=15):
    """
    Focus on working for m minutes, and then rest for r minutes.
    By default, m=45, r=15.
    """
    while True:
        sleep(m * 60)
        winsound.Beep(1000, 3000)
        sleep(r * 60)
        winsound.Beep(1000, 3000)
