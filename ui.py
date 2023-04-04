import sys
import PyQt5.QtGui as Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from chat import Chat

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.chat = Chat()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("KIM'S CHATBOT")
        self.resize(640,360)
        layout = QGridLayout()
        label1 = QLabel('<font size="5"> Hello </font>')
        layout.addWidget(label1, 0, 0)
        self.label2 = QLabel('<font size="8"> How can I help you? </font>')
        self.user_input = QLineEdit()
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.user_input, 2, 0)
        button_send = QPushButton('Send')
        layout.addWidget(button_send, 3, 0, 2, 2)
        button_send.clicked.connect(self.get_sys_response)
        self.setLayout(layout)

    def get_sys_response(self):
        sys_res = self.chat.response(self.user_input.text())
        self.label2.setText(sys_res)
