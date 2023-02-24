import sys
import os
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window. ui_main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Curso de PySide6')

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # SHOW APPLICATION
        self.show()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    sys.exit(app.exec())
