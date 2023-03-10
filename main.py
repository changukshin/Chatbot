#main

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
#UI class
class UI(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("KIM'S CHATBOT")
    self.resize(640,360)
    layout = QGridLayout()
    label1 = QLabel('<font size="5"> Hello </font>')
    #self.user_obj = QLineEdit()
    layout.addWidget(label1, 0, 0)
    #layout.addWidget(self.user_obj, 0, 1)
    label2 = QLabel('<font size="8"> How can I help you? </font>')
    self.user_pwd = QLineEdit()
    layout.addWidget(label2, 1, 0)
    layout.addWidget(self.user_pwd, 2, 0)
    button_login = QPushButton('CLICK TO BEGIN')
    layout.addWidget(button_login, 3, 0, 2, 2)
    self.setLayout(layout)
app = QApplication(sys.argv)
form = UI()
form.show()
sys.exit(app.exec_())