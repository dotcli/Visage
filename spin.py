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
alpha = 0.01
step = 0
colorWhite = [255, 255, 255]
strip.brightness = alpha
strip.fill(colorWhite)

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

def spin(strip, step):
	"""Spin a pixel on each neopixel jewel"""
	"""Skip center pixel"""
	p1Index = step % 6 + 1
	p2Index = p1Index + 7
	p3Index = p2Index + 7
	strip[p1Index] = colorWhite
	strip[p2Index] = colorWhite
	strip[p3Index] = colorWhite

while True:  # Loop forever...
	strip.fill([0, 0, 0])
	spin(strip, step)
	step = (step + 1) % 6
	strip.write()
	time.sleep(0.016)