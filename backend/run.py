# Runs the backend for Susanna
import time
from lights import LEDs

leds = LEDs(150, 0.5)
strip = leds.init_leds()


leds.display_color(strip, 255, 255, 255)
time.sleep(10)
leds.display_color(strip, 0, 0, 0)
