from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
class exercise:
    def __init__(self,label):
        self.font=QFont("Times", 24)
        label.setFont(self.font)
        
    keys=['`','1','2','3','4','5','6','7','8','9','0','-','=','backspace',
        'tab','Q','W','E','R','T','Y','U','I','O','P','[',']','fs',
        'capslock','A','S','D','F','G','H','J','J','K','L',';','sk','Enter',
        'shift','Z','X','C','V','B','N','M',',','.','/','shift',
        'ctrl','fn','home','alt','space','alt','option','ctrl',
        ]

    exercise1="""
                    asdf;lkjasdf;lkjasdf;lkjasdf;lkjasdf;lkj
                    fdsajkl;fdsajkl;fdsajkl;fdsajkl;fdsajkl;

                    """
    exercise2="""
                    asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj
                    fdsa jkl; fdsa jkl; fdsa jkl; fdsa jkl;
                    """
    exercise3="""
                    sad lad dad all add ask ass as;
                    asks alas fall dads flak lass lads add;
                    """
    exercise4="""
                    salad; a flask; a jaffa; flak falls;
                    a lass adds a jaffa as a lad asks
                    as sad as a lass; a flask falls
                    all salads add jaffas as dad asks
                    alas a sad dad; a lass adds a flask
                    a lass adds; a dad asks all; ask a lad
                    """

    
    