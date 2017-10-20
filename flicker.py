### This is the script powering trisight halloween costume, running on Adafruit GEMMA M0 running CircuitPython
import board
import neopixel
import time
try:
	import urandom as random  # for v1.0 API support
except ImportError:
	import random

# numpix = 17         # Number of NeoPixels
numpix = 21         # Number of NeoPixels
pixpin = board.D1   # Pin where NeoPixels are connected
strip  = neopixel.NeoPixel(pixpin, numpix)

minAlpha   = 0.1    # Minimum brightness
maxAlpha   = 0.1    # Maximum brightness
alpha      = (minAlpha + maxAlpha) / 2  # Start in middle
alphaDelta = 0.0008  # Amount to change brightness each time through loop
alphaUp    = True   # If True, brightness increasing, else decreasing

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions. In the order of r-g-b"""
	if pos < 85:
		return [255 - pos * 3, pos * 3, 0]
	elif pos < 170:
		pos -= 85
		return [0, 255 - pos * 3, pos * 3]
	else:
		pos -= 170
		return [pos * 3, 0, 255 - pos * 3]

# strip.fill([80, 0, 255])  # Fill red, or change to R,G,B of your liking
pos = 0
# for i in range(len(strip)):
# 	strip[i] = wheel(pos % 255)
# 	pos += 20

while True:  # Loop forever...
	if random.randint(1, 5) == 5:       # 1-in-5 random chance
		alphaUp = not alphaUp       # of reversing direction
	if alphaUp:                         # Increasing brightness?
		alpha += alphaDelta         # Add some amount
		if alpha >= maxAlpha:       # At or above max?
			alpha   = maxAlpha  # Limit to max
			alphaUp = False     # and switch direction
	else:                               # Else decreasing brightness
		alpha -= alphaDelta         # Subtract some amount
		if alpha <= minAlpha:       # At or below min?
			alpha   = minAlpha  # Limit to min
			alphaUp = True      # and switch direction

	pos += 1
	strip.fill(wheel(pos % 255))
	strip.brightness = alpha            # Set brightness to 0.0 to 1.0
	strip.write()                       # and issue data to LED strip