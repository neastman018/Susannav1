# Runs the backend for Susanna
import time
import colors
from lights import LEDs
from button.button import Button
import RPi.GPIO as GPIO


button1 = Button(pin=8)
button2 = Button(pin=10)
button3= Button(pin=11)
leds = LEDs(150, 0.5)
strip = leds.init_leds()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button1.init_button()
button2.init_button()
button3.init_button()


# state = {OFF, LED_RED, LED_GREEN}
state = "OFF"

while True:

    if state == "OFF":
        leds.off(strip)
        print("OFF")

        if button1.button_press():
            state == "OFF"
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            leds.display_color(strip, colors.GREEN)
    
    if state == "RED":
        leds.display_color(strip, colors.RED)
        print("RED")

        if button1.button_press():
            state == "OFF"
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            leds.display_color(strip, colors.GREEN)       



    elif state == "GREEN":
        leds.display_color(strip, colors.GREEN)
        print("GREEN")

        if button1.button_press():
            state == "OFF"
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            leds.display_color(strip, colors.GREEN)       


    else:
        print("INVALID STATE")
        
        if button1.button_press():
            state == "OFF"
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            leds.display_color(strip, colors.GREEN)
