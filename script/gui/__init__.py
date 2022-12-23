# gui/__init__.py
# Handles main gui functions


# Imports
from PySide6 import QtWidgets

from gui.ui_startup import Ui_main_window


# Definitions
class main_window(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)