# Runs the backend for Susanna
import time
import colors
from lights import LEDs


leds = LEDs(150, 0.5)
strip = leds.init_leds()


leds.display_color(strip, colors.OREGANO)
time.sleep(10)
leds.display_color(strip, r=200, g=200)
time.sleep(10)
leds.display_color(strip, r=93, b=111, g=64)
time.sleep(10)
leds.off(strip)
