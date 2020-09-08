"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

ndx = 9

while True:
    if ndx == -1:
        ndx = 9
    if ndx >= 10:
        ndx = 0

    cp.pixels[ndx] = (255,255,255)
    sleep(0.5)
    cp.pixels[ndx] = (0,0,0)

    if cp.switch:
        ndx += 1
    else:
        ndx -= 1



# cp.pixels.brightness = 1

# while True:
#     if cp.switch:
#         for i in range (0, 10):
#             cp.pixels[i] = (255,255,255)
#             sleep(0.5)
#             cp.pixels[i] = (0,0,0)
#             sleep(0)
#     else:
#         for i in range (0, 10):
#             cp.pixels[9-i] = (255,255,255)
#             sleep(0.5)
#             cp.pixels[9-i] = (0,0,0)
#             sleep(0)