"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp

while True:
    cp.pixels[0] = (139,0,0)
    cp.pixels[1] = (220,20,60)
    cp.pixels[2] = (255,0,0)
    cp.pixels[3] = (205,92,92)
    cp.pixels[4] = (255,99,71)
    cp.pixels[5] = (250,128,114)
    cp.pixels[6] = (255,160,122)
    cp.pixels[7] = (255,99,71)
    cp.pixels[8] = (255,69,0)
    cp.pixels[9] = (219,112,147)
