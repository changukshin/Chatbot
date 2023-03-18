import sys
import ui
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_instance = ui.UI()
	ui_instance.show()
	sys.exit(app.exec_())
