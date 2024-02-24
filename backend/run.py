# Runs the backend for Susanna
import time
from lights import LEDs

strip = LEDs(150, 0.5)

strip.display_color(255, 255, 255)
time.sleep(10)
strip.display_color(0, 0, 0)
