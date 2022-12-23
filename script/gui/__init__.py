# gui/__init__.py
# Handles main gui functions


# Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from os import getcwd, system

from gui import ui_startup
from gui import ui_test_create


# Definitions

# Window handlers
class StartWindow(QMainWindow, ui_startup.Ui_main_window):
    def __init__(self):
        # Init
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        self.setWindowTitle("Py-Grader: Start menu")
        
        # Button connections
        self.new_test_button.clicked.connect(test_create_start)


class TestCreateWindow(QMainWindow, ui_test_create.Ui_main_window):
    def __init__(self):
        # Init
        super(TestCreateWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        self.setWindowTitle("Py-Grader: Test Creation")
        
        # Button connections
        self.nerd_mode_button.clicked.connect(open_nerd_mode)

def create_windows() -> None:
    global start_window 
    global test_create_window
    
    start_window = StartWindow()
    test_create_window = TestCreateWindow()


# Button methods

# Window changers
def test_create_start() -> None:
    test_create_window.show()


# Other button methods
def open_nerd_mode() -> None:
    system(f"code \"{getcwd()}\\tests\"")