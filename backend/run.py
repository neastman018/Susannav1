# Runs the backend for Susanna
import time
import colors
from lights import LEDs


leds = LEDs(150, 0.5)
strip = leds.init_leds()


leds.display_color(strip, colors.OREGANO)
time.sleep(10)
leds.display_color(strip, 200, 200, 0)
time.sleep(10)
leds.off(strip)
