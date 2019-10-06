import math
from PyQt5.QtCore import QTimer


class Timer:
    def __init__(self,interval):
        self.timer=QTimer()
        self.timer.setInterval(interval*1000)
        self.current_time=0
        self.isplaying=False
        self.ispaused=False
        self.isstopped=False
        self.display_time=0

    def set_slot(self,slot):
        self.timer.timeout.connect(slot)


    def stop(self):
        self.timer.stop()
        self.current_time=0
        self.isstopped=True
        self.isplaying=False 

    def pause(self):
        self.timer.stop()
        self.ispaused=True 
        self.isplaying=False

    def play(self):
        if self.isstopped:
            self.timer.start()
        if self.ispaused:
            self.timer.start()
        self.isplaying=True 

    def update_timer(self):
        self.current_time+=1
    
    @property
    def display_time(self):
        minutes=math.floor(self.current_time/59)
        mm= minutes if minutes >9 else f"0{minutes}"
        seconds=self.current_time%59
        ss= seconds if seconds >9 else f"0{seconds}"
        return f"{mm}:{ss}"

    @display_time.setter
    def display_time(self,x):
        pass
        