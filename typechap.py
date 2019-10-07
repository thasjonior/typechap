import sys
import math

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLabel,QVBoxLayout,QGroupBox,QHBoxLayout

from timer import Timer
from exercise import exercise

class MainApp(QWidget): 
    def __init__(self):
        super().__init__()
        self.speedCounter=Timer(1)
        self.speedCounter.set_slot(self.speedCounter.update_timer)
        self.exerciseCounter=Timer(120)
        self.exerciseCounter.set_slot(self.callnext_exercise)
        self.textfield=QLabel(self)
        self.keyboard=QGroupBox(self)
        self.Timer=QHBoxLayout()
        self.btn_status="start"
        self.timer_label=QLabel("mm:ss")
        self.Timer.addWidget(self.timer_label)
        self.Timer.addWidget(self.get_play_pause_btn())
        self.Timer.addWidget(self.stop_btn())
        self.exercise=exercise(self.textfield)
        self.initUI()
        self.next_exercise=1
        


    def initUI(self):
        self.create_layout()
        self.set_keyboard_keys()
        self.display_time()
        self.setGeometry(1000,1000,1000,600)
        self.setWindowTitle("T.Y.P.E...CHAP")
        self.show()

    def create_layout(self):
        box=QVBoxLayout(self)
        box.addLayout(self.Timer)
        box.addWidget(self.textfield)
        box.addWidget(self.keyboard)

    def set_keyboard_keys(self):
        grid=QGridLayout(self)
        position=[(row,column) for row in range(5) for column in range(14) ]
        for position,key in zip(position,self.exercise.keys):
            btn=QPushButton(key,self)
            grid.addWidget(btn,*position)
 
        self.keyboard.setLayout(grid)

    # def timer_label(self):
    #     return QLabel("mm:ss",self)
    
    # @property
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
        else:
            self.btn_status="resume"
            self.speedCounter.pause()
        self.play_pause_btn.setText(self.btn_status)

    # @property
    def stop_btn(self):
        btn=QPushButton("stop",self)
        btn.setFixedSize(100,30)
        btn.clicked.connect(self.stop)
        return btn

    def stop(self):
        self.speedCounter.stop()
        self.btn_status="start"
        self.play_pause_btn.setText(self.btn_status)
             

    def display_time(self):
        self.timer_label.setText (self.speedCounter.display_time)
        self.speedCounter.play()
        # self.change_starstop_btn()


            

            




    # def change_starstop_btn(self):
    #     self.textfield.setText(self.exercise.exercises[0])

    #     if self.btn_status.text()=="start":
    #         self.btn_status.setText("stop")
    #         timer.start()
    #     else:
    #         self.btn.setText("start")
    #         timer.stop()
    #         self.next_exercise=1
    #         self.current_time=0
            
            

    def callnext_exercise(self):
        self.current_time=0
        self.textfield.setText(self.exercise.exercises[self.next_exercise])
        self.next_exercise+=1

   
        

if __name__ =='__main__':
    app=QApplication(sys.argv)
    main=MainApp()
    sys.exit(app.exec_())