"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep

while True:
    # display.scroll("Hello World!")
    # display.show(Image.HAPPY)
    # boat = Image("05050:"
    #             "05050:"
    #             "05050:"
    #             "99999:"
    #             "09990")

    # display.show(boat)
    # display.show(Image.ALL_ARROWS, loop=True, delay=1000)
    dot = Image("90000:00000:00000:00000:00000")
    display.show(dot)
    sleep(1) 