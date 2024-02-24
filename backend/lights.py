# Methods for LED Lights
import time
import board
import neopixel



class LEDs:
    """
    @param leds is the led strip
    @param num_pixels is the number of pixels on the strip
    @param brightness is the brightness of the LEDs from 0-1
    @param auto_write: False, pixels do not auto update (need pixels.show())
                       True, Pixels auto update
    @param pixel pin: # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
                      # NeoPixels must be connected to D10, D12, D18 or D21 to work.

    """
    def __init__(self, num_pixels, brightness = 0.5, auto_write = True, pixel_pin = board.D18, pixel_order = neopixel.RGB):
        self.num_pixels = num_pixels
        self.brightness = brightness
        self.auto_write = auto_write
        self.pixel_pin = pixel_pin
        self.pixel_order = pixel_order


        
    def init_leds(self):
        strip = neopixel.NeoPixel(
            pixel_pin = board.D18, num_pixels = 150, brightness=0.2, auto_write=False, pixel_order = neopixel.GRB
)
        return strip

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.


    def wheel(self, strip, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.pixel_order in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    """
    @param wait is the time between cycles in seconds
    """
    def rainbow_cycle(self, strip, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                strip[i] = self.wheel(pixel_index & 255)
            if not self.auto_write:
                strip.show()
            time.sleep(wait)


    """
    Method to display a color
    """
    def display_color(self, strip, r, b, g):
        strip.fill((r, b, g))




