import sys
from exercise import exercise
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLabel,QVBoxLayout,QGroupBox,QHBoxLayout

class mainapp(QWidget):
    def __init__(self):
        super().__init__()
        self.textfield=QLabel(self)
        self.keyboard=QGroupBox(self)
        self.Timer=QHBoxLayout()
        self.execise=exercise(self.textfield)
        self.initUI()

    def initUI(self):
        self.create_layout()
        self.set_time()
        self.set_keyboard_keys()
        self.setGeometry(1000,1000,1000,600)
        self.setWindowTitle("T.Y.P.E...CHAP")
        self.show()

    def create_layout(self):
        box=QVBoxLayout(self)
        box.addLayout(self.Timer)
        box.addWidget(self.textfield)
        box.addWidget(self.keyboard)

    def set_keyboard_keys(self):
        self.textfield.setText(self.execise.exercise4)
        grid=QGridLayout(self)
        position=[(row,column) for row in range(5) for column in range(14) ]
        for position,key in zip(position,self.execise.keys):
            btn=QPushButton(key,self)
            grid.addWidget(btn,*position)
 
        self.keyboard.setLayout(grid)

    def set_time(self):
        self.timer=QLabel("00:00",self)
        self.btn=QPushButton("start",self)
        self.btn.setFixedSize(100,30)
        self.btn.clicked.connect(self.count_time)
        self.Timer.addWidget(self.timer)
        self.Timer.addWidget(self.btn)

    def count_time(self):
        self.change_starstop_btn()


    def change_starstop_btn(self):
        timer=QTimer(self)
        timer.setInterval(5*60)
        if self.btn.text()=="start":
            self.btn.setText("stop")
            timer.start()
        else:
            self.btn.setText("start")
            timer.stop()


        
        

if __name__ =='__main__':
    app=QApplication(sys.argv)
    main=mainapp()
    sys.exit(app.exec_())