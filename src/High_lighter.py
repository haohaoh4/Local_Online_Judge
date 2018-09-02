import os
import sys
from PyQt5.QtCore import (QEvent, QFile, QFileInfo, QIODevice, QRegExp,
                          QTextStream,Qt)
from PyQt5.QtWidgets import (QAction, QApplication,  QFileDialog,
                             QMainWindow, QMessageBox, QTextEdit)
from PyQt5.QtGui import (QFont, QIcon,QColor,QKeySequence,QSyntaxHighlighter,QTextCharFormat,QTextCursor)


class HighLighter(QSyntaxHighlighter):
	def __init__(self, parent=None):
		super().__init__()
