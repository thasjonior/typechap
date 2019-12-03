import sys

from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout, QLabel
from PyQt5.Qt import QApplication
from PyQt5.QtCore import Qt

from exercise import Exercise
from styles import Style
from dataSource import Source

class Canvas(QWidget):
    """
    Place where exercise text is displayed.
    It should be initialized with the exercise.
    It performs manipulations on the exercise by updating progress,
    indicating what the user has typed and updates how many successes or
    failure the user makes
    We implement the main keyPressEvent here to capture all key strokes and process accordingly.
    
    """

    def __init__(self,parent,exercise):
        super().__init__()
        self.parent = parent
        self.show()
        self.exercise = exercise
        layout = QVBoxLayout()

        
        self.text_viewer = QTextEdit(self) # QTextEdit allows for rich text editing.
        self.typing_area = QTextEdit(self)
        self.text_viewer.setReadOnly(True)
        self.typing_area.setReadOnly(True)
        self.text_viewer.setHtml(f'<p style="font-size: 22px;">{self.exercise.text}</p>')
        self.setFocusPolicy(Qt.ClickFocus) # only set focus when this is clicked
        self.typing_area.show()
        layout.addWidget(self.text_viewer)
        layout.addWidget(self.typing_area)
        # layout.addWidget(QLabel("Click here to get started"))
        self.setLayout(layout)
    
    def keyPressEvent(self, key_event):
        code = key_event.key()
        char = key_event.text()
        print(f"{code}:{char}")
        if code == 32: #space
            char = '<span style="font-size: 22px;">&nbsp;</span>'
        elif code == 75 and self.exercise.current_char == '\n': # enter
            char = '<span>'
        elif self.exercise.current_char != char:
            char = f'<span style="color: #ff0000; font-size: 22px;">{char}</span>'
        else:
            self.exercise.add_passes()
            char = f'<span style="color: #0000ff; font-size: 22px;">{char}</span>'
        self.exercise.next_char()
        self.typed(char)
        print(self.exercise.live_score)
            
    def typed(self, char):
        self.typing_area.insertHtml(char)

# if __name__ == '__main__':
#     qapp = QApplication(sys.argv)
#     aa=Source(1)
#     app = Canvas(Exercise("exercise 1",aa.container[0]))
#     app.setGeometry(200, 300, 500, 600)
#     app.show()
#     sys.exit(qapp.exec_())