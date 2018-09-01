# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sat Sep  1 23:15:40 2018
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton)


class MainWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setup_ui(main_window)
        main_window.show()

    def setup_ui(self, window):
        window.setObjectName("MainWindow")
        window.resize(800, 600)
        bt = QPushButton('Button', window)
        bt.move(300, 200)
        bt.setToolTip("This is a <b>button</b>!")
        window.setGeometry(300, 300, 300, 300)

