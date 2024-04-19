# Runs the backend for Susanna
import time
from button.button import Button
import RPi.GPIO as GPIO
from subprocess import run
import pygame
from alarm.alarm import Alarm


def turn_on_display():
    run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --on", shell=True)
    return True

def turn_off_display():
    run("WAYLAND_DISPLAY='wayland-1' wlr-randr --output HDMI-A-1 --off", shell=True)
    return False



button1 = Button(pin=14)
button2 = Button(pin=15)
button3= Button(pin=17)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button1.init_button()
button2.init_button()
button3.init_button()

alarm = Alarm()
alarm.init_alarm("Good_MorningV2.mp3")

# state = {OFF, ALARM_ACTIVE, ON}
state = "ON"
display = False

while True:

    if state == "OFF":
        alarm.play_alarm_on_time(12, 0)
        if alarm.is_active():
            state = "ALARM_ACTIVE"
            display = turn_on_display()
        if button1.button_press():
            state = "ON"
            display = turn_on_display()

    elif state == "ON":
        if button2.button_press():
            state == "OFF"
            display = turn_off_display()

    elif state == "ALARM_ACTIVE":
        if button3.button_press():
            alarm.alarm_stop()
            state == "ON"

    else:
        print("Invalid State -- Defaulting to On")
        if alarm.is_active():
            alarm.alarm_stop()
        if display == False:
            display = turn_on_display()




