
from PyQt5.Qt import QColor
class Style:

    @staticmethod
    def set_red_color(widget):
        widget.setColor(QColor(255, 0, 0, 0.8))

    @staticmethod
    def set_blue_color(widget):
        widget.setColor(QColor(0, 0, 255, 0.9))