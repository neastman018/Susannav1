# Runs the backend for Susanna
import time
from button.button import Button
import RPi.GPIO as GPIO
from subprocess import run


button1 = Button(pin=14)
button2 = Button(pin=15)
button3= Button(pin=17)

GPIO.setwarnings(False)
button1.init_button()
button2.init_button()
button3.init_button()


# state = {OFF, LED_RED, LED_GREEN}
state = "OFF"

while True:
    if button1.button_press():
        state = "OFF"
        print("OFF")
        run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --off", shell=True)
    elif button2.button_press():
        state = "RED"
        print("RED")
        run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --on", shell=True)
    elif button3.button_press():
        state = "GREEN"
        print("GREEN")
        run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --on", shell=True)
    # if state == "OFF":
    #     if button1.button_press():
    #         state = "OFF"
    #         print("OFF")
    #         leds.off(strip)
    #     elif button2.button_press():
    #         state = "RED"
    #         print("RED")
    #         leds.display_color(strip, 255, 0, 0)
    #     elif button3.button_press():
    #         state = "GREEN"
    #         print("GREEN")
    #         leds.display_color(strip, 0, 255, 0)

    
    # elif state == "RED":
    #     if button1.button_press():
    #         state = "OFF"
    #         print("OFF")
    #         leds.off(strip)
    #     elif button2.button_press():
    #         state = "RED"
    #         print("RED")
    #         leds.display_color(strip, 255, 0, 0)
    #     elif button3.button_press():
    #         state = "GREEN"
    #         print("GREEN")
    #         leds.display_color(strip, 0, 255, 0)



    # elif state == "GREEN":
    #     if button1.button_press():
    #         state = "OFF"
    #         print("OFF")
    #         leds.off(strip)
    #     elif button2.button_press():
    #         state = "RED"
    #         print("RED")
    #         leds.display_color(strip, 255, 0, 0)
    #     elif button3.button_press():
    #         state = "GREEN"
    #         print("GREEN")
    #         leds.display_color(strip, 0, 255, 0)
     


    # else:
    #     print("INVALID STATE")
    #     if button1.button_press():
    #         state = "OFF"
    #         print("OFF")
    #         leds.off(strip)
    #     elif button2.button_press():
    #         state = "RED"
    #         print("RED")
    #         leds.display_color(strip, 255, 0, 0)
    #     elif button3.button_press():
    #         state = "GREEN"
    #         print("GREEN")
    #         leds.display_color(strip, 0, 255, 0)
