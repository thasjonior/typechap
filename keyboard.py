from PyQt5.QtWidgets import QWidget,QGridLayout, QVBoxLayout,QApplication, QPushButton
import sys
from PyQt5 import  QtCore

class Keyboard(QWidget):
    """
    this class manages the on screen keyboard
    """
    def __init__(self):
        super().__init__()
        self.btn=QPushButton("btn",self)
        self.keys=['1','2','3','4','5','6','7','8','9','0','-','=','backspace',
        'tab','q','w','e','r','t','y','u','i','o','p','[',']','fs',
        'cl','a','s','d','f','g','h','j','k','l',';','quote','Enter',
        'shift','z','x','c','v','b','n','m',',','.','/','shift'
        'crt','fn','home','alt','space','alt','options','ctr',
        ]
        self.initUI()

    def initUI(self):
        pass
        # self.setGeometry(1000,500,1000,500)
        # self.show()

    @property
    def onscreen_keyboard(self):
        print('hi')
        grid=QGridLayout(self)
        position=[(row,column) for row in range(5) for column in range(14) ]
        for position,key in zip(position,self.keys):
            btn=QPushButton(key,self)
            grid.addWidget(btn,*position)
        grid.setGeometry(QtCore.QRect(100,100,100,100))
        return grid

        

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     key=Keyboard()
#     sys.exit(app.exec_())


