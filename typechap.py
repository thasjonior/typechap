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
        self.cur_ex = 0
        self.btn_status="start"
        self.speedCounter=Timer(1)
        self.speedCounter.set_slot(self.speedCounter.update_timer)
        self.exerciseCounter=Timer(120)
        self.source=Source()# sourcedata class
        self.keyboard=Keyboard(self)
        self.exercise=Exercise('exercise',self.source.container[self.source.cur_ex])
        self.canvas=Canvas(self,self.exercise)
        self.layout=QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(1000,700,1000,700)
        self.setWindowTitle('T.Y.P.E.CHAP')
        self.displayLayout()
        self.display_time()
        self.show()

    def displayLayout(self):
        self.leftbox=QHBoxLayout(self)
        self.leftbox.addWidget(self.canvas)
        grid=QGridLayout(self)
        self.label=QLabel("00:00")
        self.start_btn=QPushButton("start")
        # self.stop_btn=QPushButton("stop")
        self.open_btn=QPushButton("previous")
        self.open_btn.clicked.connect(self.call_prev_exercise)
        self.nxt_btn=QPushButton("next")
        self.nxt_btn.clicked.connect(self.call_next_exercise)
        grid.addWidget(self.timer_label,0,0)
        grid.addWidget(self.get_play_pause_btn,1,0)
        grid.addWidget(self.stop_btn,1,1)
        grid.addWidget(self.open_btn,2,0)
        grid.addWidget(self.nxt_btn,2,1)
        self.leftbox.addLayout(grid)
        self.layout.addLayout(self.leftbox) 
        self.layout.addWidget(self.keyboard)
        self.setLayout(self.layout)



    def call_next_exercise(self):
        self.source.next_ex()
        self.remove_widget()
        self.exercise=Exercise('exercise',self.source.container[self.source.cur_ex])
        self.canvas=Canvas(self,self.exercise)
        self.leftbox.addWidget(self.canvas)
        
    def call_prev_exercise(self):
        self.source.prev_ex()
        self.remove_widget()
        self.exercise=Exercise('exercise',self.source.container[self.source.cur_ex])
        self.canvas=Canvas(self,self.exercise)
        self.leftbox.addWidget(self.canvas)


    def remove_widget(self):
        """removes previous widet
        pass previous widget
        """
        self.leftbox.removeWidget(self.canvas)
        self.canvas.hide()

    @property
    def timer_label(self):
        try:
            if self.label:
                pass
        except AttributeError:
                self.label=QLabel("mm:ss",self)
        return self.label
    
    @property
    def get_play_pause_btn(self):
        try:
            if self.play_pause_btn:
                return self.play_pause_btn
        except AttributeError as e:
            self.play_pause_btn=QPushButton(self.btn_status,self)
            self.play_pause_btn.setFixedSize(100,30)
            self.play_pause_btn.clicked.connect(self.play_pause)
        return self.play_pause_btn

    def play_pause(self):
        if self.btn_status == "start" or self.btn_status=="resume":
            self.btn_status="pause"
            self.speedCounter.play()
            self.exerciseCounter.play()
        else:
            self.btn_status="resume"
            self.speedCounter.pause()
            self.exerciseCounter.pause()
        self.play_pause_btn.setText(self.btn_status)

    @property
    def stop_btn(self):
        btn=QPushButton("stop",self)
        btn.setFixedSize(100,30)
        btn.clicked.connect(self.stop)
        return btn

    def stop(self):
        self.speedCounter.stop()
        self.exerciseCounter.stop()
        self.btn_status="start"
        self.play_pause_btn.setText(self.btn_status)
        self.label.setText(self.speedCounter.display_time)
             
    
    def display_time(self):
        self.timer_label.setText(self.speedCounter.display_time)
        self.speedCounter.play()
        
        
    def update_timer(self):
        self.speedCounter.update_timer()
        self.label.setText(self.speedCounter.display_time) 






   
if __name__ =='__main__':
    app=QApplication(sys.argv)
    main=MainApp()
    sys.exit(app.exec_())