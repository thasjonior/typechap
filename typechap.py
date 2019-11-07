import sys
import math

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLabel,QVBoxLayout,QGroupBox,QHBoxLayout

from timer import Timer
from canvas import Canvas
from exercise import Exercise
from dataSource import Source
from keyboard import Keyboard

class MainApp(QWidget): 
    def __init__(self):
        super().__init__()
        
        self.keyboard=Keyboard()
        self.source=Source(0)
        self.exercise=Exercise('one',self.source.container[2])
        self.canvas=Canvas(self.exercise)
        self.canvas.setGeometry(200, 300, 500, 600)
        self.canvas.show()
        self.layout=QVBoxLayout()
        self.initUI()
    def initUI(self):
        # self.layout.addLayout(self.keyboard.onscreen_keyboard)
        self.layout.addWidget(self.keyboard.btn.show())
        # self.layout.addLayout(self.canvas)
        self.setGeometry(1000,1000,1000,600)
        self.setWindowTitle("T.Y.P.E...CHAP")
        self.show()
    #     self.textfield=QLabel(self)()
    #     self.Timer=QHBoxLayout()
    #     self.btn_status="start"
    #     self.Timer.addWidget(self.timer_label)
    #     self.Timer.addWidget(self.get_play_pause_btn())
    #     self.Timer.addWidget(self.stop_btn())
        
        

    #     self.speedCounter=Timer(1)
    #     self.speedCounter.set_slot(self.speedCounter.update_timer)
    #     self.exerciseCounter=Timer(120)
    #     self.next_exercise=0
    #     # self.callnext_exercise()
    #     # self.exerciseCounter.set_slot(self.callnext_exercise)
    #     self.initUI()


    # def initUI(self):
    #     self.create_layout()
    #     # self.set_keyboard_keys()
    #     self.display_time()
    #     self.setGeometry(1000,1000,1000,600)
    #     self.setWindowTitle("T.Y.P.E...CHAP")
    #     self.show()

    # def create_layout(self):
    #     box=QVBoxLayout(self)
    #     box.addLayout(self.Timer)
    #     box.addWidget(self.textfield)
    #     keyboard=self.keyboard.onscreen_keyboard
    #     # keyboard.setGeometry(QRect(1000,500,1000,1000))
    #     box.addLayout(keyboard)
        


 
        

    # @property
    # def timer_label(self):
    #     try:
    #         if self.label:
    #             pass
    #     except AttributeError:
    #             self.label=QLabel("mm:ss",self)
    #     return self.label
    
    # # @property
    # def get_play_pause_btn(self):
    #     try:
    #         if self.play_pause_btn:
    #             return self.play_pause_btn
    #     except AttributeError as e:
    #         self.play_pause_btn=QPushButton(self.btn_status,self)
    #         self.play_pause_btn.setFixedSize(100,30)
    #         self.play_pause_btn.clicked.connect(self.play_pause)
    #     return self.play_pause_btn

    # def play_pause(self):
    #     if self.btn_status == "start" or self.btn_status=="resume":
    #         self.btn_status="pause"
    #         self.speedCounter.play()
    #         self.exerciseCounter.play()
    #     else:
    #         self.btn_status="resume"
    #         self.speedCounter.pause()
    #         self.exerciseCounter.pause()
    #     self.play_pause_btn.setText(self.btn_status)

    # # @property
    # def stop_btn(self):
    #     btn=QPushButton("stop",self)
    #     btn.setFixedSize(100,30)
    #     btn.clicked.connect(self.stop)
    #     return btn

    # def stop(self):
    #     self.speedCounter.stop()
    #     self.exerciseCounter.stop()
    #     self.btn_status="start"
    #     self.play_pause_btn.setText(self.btn_status)
    #     self.label.setText(self.speedCounter.display_time)
             
    
    # def display_time(self):
    #     self.timer_label.setText(self.speedCounter.display_time)
    #     self.speedCounter.play()
        
        
    # def update_timer(self):
    #     self.speedCounter.update_timer()
    #     self.label.setText(self.speedCounter.display_time) 

    # def callnext_exercise(self):
    #     self.textfield.setText(self.exercise.exercises[self.next_exercise])
    #     self.next_exercise+=1

   
if __name__ =='__main__':
    app=QApplication(sys.argv)
    main=MainApp()
    sys.exit(app.exec_())