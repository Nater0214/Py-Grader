# gui/__init__.py
# Handles main gui functions


# Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6 import QtCore as Qt

import os
import sys

from . import ui_startup
from . import ui_test_create
from . import ui_test_run

sys.path.append(os.path.abspath(""))

import tests


# Definitions

# Window handlers
class StartWindow(QMainWindow, ui_startup.Ui_main_window):
    def __init__(self, app: QApplication):
        # Init
        
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        
        self.app = app
        
        # Button connections
        self.run_test_button.clicked.connect(self.test_run_start)
        self.new_test_button.clicked.connect(self.test_create_start)
    
    
    def closeEvent(self, event) -> None:
        self.app.quit()
    
    
    # Window changers
    def test_run_start(self) -> None:
        # Opens the test run window

        test_run_window.show()


    def test_create_start(self) -> None:
        # Opens the test creation window

        test_create_window.show()


class TestCreateWindow(QMainWindow, ui_test_create.Ui_main_window):
    def __init__(self):
        # Init
        
        super(TestCreateWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        
        # Button connections
        self.nerd_mode_button.clicked.connect(self.open_nerd_mode)
    
    # Button methods
    def open_nerd_mode(self) -> None:
        # Opens the nerd mode for making tests

        os.system(f"code \"{os.getcwd()}\\tests\"")


class TestRunWindow(QMainWindow, ui_test_run.Ui_main_window):
    def __init__(self):
        # Init
        
        super(TestRunWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        self.display_tests()
        
        # Button connections
        self.test_run_button.clicked.connect(self.run_test)
    
    
    def display_tests(self) -> None:
        self.tests_list.addItems(tests.get_test_names())
    
    
    def run_test(self) -> None:
        tests.run_test(self.tests_list.currentItem().text())


def create_windows(app: QApplication) -> None:
    global start_window 
    global test_create_window
    global test_run_window
    
    start_window = StartWindow(app)
    test_create_window = TestCreateWindow()
    test_run_window = TestRunWindow()