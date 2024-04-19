"""
Methods for setting and activating an alarm
"""
import multiprocessing
import pygame
from datetime import datetime 
import string

"""
Function to inteperate time 
"""
#def interperate_time(time):

"""
Method to initalize the alarm
@parameter alarm_sound: music file to play
"""

"""
Method to play the alarm
@param alarm: return of the init_alarm function which is a initalized alarm with a song loaded
"""

class Alarm:

    def __init__(self, alarm = pygame.mixer.music):
        self.alarm = alarm

        


    def init_alarm(self, alarm_sound):
        self.alarm.load("alarm/music/" + alarm_sound)

        print(f"Alarm playing {alarm_sound} is ready")
    
    """
    Getter Method for the alarm being active
    @return true if alarm is playing and false if not
    """
    def is_active(self) -> bool:
        return self.alarm.get_busy()
    

    def play_alarm(self):
        self.alarm.play()
        
    """
    Plays the alarm at a certain time
    @param hour, minute is the time to play
    """
    def play_alarm_on_time(self, hour, minute) -> bool:
        now = datetime.now()

        if hour == now.hour and minute == now.minute and not self.is_active():
            print(self.is_active())
            self.alarm.play()
    
    # Method to stop the alarm if active
    def alarm_stop(self)->bool:
        if self.is_active():
            self.alarm.stop()

    if __name__ == "__main__":
        now = datetime.now()
        print(now.day)




          
           
    
