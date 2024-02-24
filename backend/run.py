# Runs the backend for Susanna
import time
import colors
from lights import LEDs
from button.button import Button
import RPi.GPIO as GPIO


button1 = Button(pin=14)
button2 = Button(pin=15)
button3= Button(pin=17)
leds = LEDs(150, 0.5)
strip = leds.init_leds()

GPIO.setwarnings(False)
button1.init_button()
button2.init_button()
button3.init_button()


# state = {OFF, LED_RED, LED_GREEN}
state = "OFF"

while True:

    if state == "OFF":
        leds.off(strip)

        if button1.button_press():
            state == "OFF"
            print("OFF")
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            print("RED")
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            print("GREEN")
            leds.display_color(strip, colors.GREEN)
    
    elif state == "RED":
        leds.display_color(strip, colors.RED)


        if button1.button_press():
            state == "OFF"
            print("OFF")
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            print("RED")
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            print("GREEN")
            leds.display_color(strip, colors.GREEN)       



    elif state == "GREEN":
        leds.display_color(strip, colors.GREEN)
        print("GREEN")

        if button1.button_press():
            state == "OFF"
            print("OFF")
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            print("RED")
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            print("GREEN")
            leds.display_color(strip, colors.GREEN)       


    else:
        print("INVALID STATE")

        if button1.button_press():
            state == "OFF"
            print("OFF")
            leds.off(strip)
        elif button2.button_press():
            state == "RED"
            print("RED")
            leds.display_color(strip, colors.RED)
        elif button3.button_press():
            state = "GREEN"
            print("GREEN")
            leds.display_color(strip, colors.GREEN)
