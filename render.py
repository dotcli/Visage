### This is the script powering trisight halloween costume, running on Adafruit GEMMA M0 running CircuitPython
import board
import neopixel
import time
try:
	import urandom as random  # for v1.0 API support
except ImportError:
	import random

numpix = 21         # Number of NeoPixels
pixpin = board.D1   # Pin where NeoPixels are connected
strip  = neopixel.NeoPixel(pixpin, numpix)
alpha = 0.1
c_white = (255, 255, 255)
c_red = (255, 0, 0)
c_black = (0, 0, 0)
strip.brightness = alpha

def render(strip, data):
	strip.fill([0,0,0])
	for i in range(len(data)):
		strip[i] = data[i]

while True:  # Loop forever...
	render(strip, [
		c_white,c_white,c_red,c_black,c_white,c_black,c_black,
		c_white,c_black,c_red,c_white,c_black,c_black,c_white,
		c_white,c_white,c_black,c_white,c_black,c_white,c_black
	])
	strip.write()
	time.sleep(0.016)