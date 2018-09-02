from src import main_ui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = QMainWindow()
	ui = main_ui.MainWindow(main_win)
	sys.exit(app.exec_())

