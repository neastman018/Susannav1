import subprocess  # for command execution                      
import RPi.GPIO as GPIO 
import time
import pygame
import multiprocessing
from datetime import datetime 
from button.button import Button

state = False
buttonPin = 10
GPIO.setwarnings(False)                                        
GPIO.setmode(GPIO.BOARD)                                        
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    

button1 = Button(buttonPin)
button1.init_button()

if __name__ == '__main__':
    pygame.mixer.init()
    alarm = pygame.mixer.music
    alarm.load('alarm/music/Good_MorningV2.mp3')      

    GPIO.setwarnings(False)                                        
    GPIO.setmode(GPIO.BOARD)                                        
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
    print("All Good in the Hood\n")

    while True:
        if button1.press() and not state:
            alarm.play()
            state = True
            print("Button is Pressed, Music should be playing\n")

        elif button1.press() and state:
            alarm.stop()
            state = False
            print("Button is Pressed, Music should stop playing\n")


            
    