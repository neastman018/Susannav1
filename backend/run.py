# Runs the backend for Susanna
import time
from lights import LEDs
from button.button import Button
import RPi.GPIO as GPIO
from datetime import datetime
import pygame
from alarm.alarm import Alarm


button1 = Button(pin=14)
button2 = Button(pin=15)
button3= Button(pin=17)
alarm = Alarm(hour=8, minute=57, second=0)
leds = LEDs(150, 0.5)
strip = leds.init_leds()

GPIO.setwarnings(False)
button1.init_button()
button2.init_button()
button3.init_button()

# state = {OFF, LED_RED, LED_GREEN, ALARM_ACTIVE}
state = "OFF"
pygame.mixer.init()
alarm.init_alarm("Good_MorningV2.mp3")




while True:
    now = datetime.now()

    if state == "ALARM_ACTIVE":
        if button1.button_press():
            state == "AlARM_OFF"
            alarm.alarm_stop(True)

    if state == "ALARM_OFF":    
        alarm.play_alarm()
        if alarm.is_active():
            state = "ALARM_ACTIVE" 
            leds.display_color(strip, 255, 255, 255)
   
        elif button1.button_press():
            print("OFF")
            leds.off(strip)
        elif button2.button_press():
            print("RED")
            leds.display_color(strip, 255, 0, 0)
        elif button3.button_press():
            print("GREEN")
            leds.display_color(strip, 0, 255, 0)















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
