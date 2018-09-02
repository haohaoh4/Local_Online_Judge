from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.Qt import QTextEdit
from PyQt5 import QtCore
import sys
from src.High_lighter import HighLighter

class MainWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setup_ui(main_window)
        main_window.show()

    def setup_ui(self, window):
        window.setObjectName("MainWindow")
        window.showMaximized()
        bt = QPushButton('Submit', window)
        bt.move(480, 480)
        bt.setToolTip("This is a <a style=\"color:red\">button</a>!")
        bt.clicked.connect(lambda: print("Hi,mouse."))
        bt.show()
        text_box = QTextEdit(window)
        text_box.move(180, 50)
        text_box.resize(700, 400)
        text_box.show()

        timer = QtCore.QTimer(window)
        timer.timeout.connect(lambda: print("aaa"))
        timer.start(1000)
        timer.timeout.connect(lambda: print("aaa"))
