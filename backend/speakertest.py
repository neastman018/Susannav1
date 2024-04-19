import subprocess  # for command execution                      
import RPi.GPIO as GPIO 
import time
import pygame
import multiprocessing
from datetime import datetime 
  

state = False
buttonPin = 10
GPIO.setwarnings(False)                                        
GPIO.setmode(GPIO.BOARD)                                        
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    

if __name__ == '__main__':
    pygame.mixer.init()
    alarm = pygame.mixer.music
    alarm.load('backend/alarm/music/Good_MorningV2.mp3')      

    GPIO.setwarnings(False)                                        
    GPIO.setmode(GPIO.BOARD)                                        
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    

    while True:
        if GPIO.input(buttonPin) == GPIO.HIGH and not state:
            alarm.play()
            state = True

        elif GPIO.input(buttonPin) == GPIO.HIGH and state:
            alarm.stop()
            state = False
    