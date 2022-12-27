# gui/__init__.py
# Handles main gui functions

# Imports
import os
import sys

from PySide6 import QtCore as Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

from . import ui_startup, ui_test_create, ui_test_results, ui_test_run

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
        """Opens the test run window"""

        test_run_window.show()


    def test_create_start(self) -> None:
        """Opens the test creation window"""

        test_create_window.show()


class TestCreateWindow(QMainWindow, ui_test_create.Ui_main_window):
    def __init__(self) -> None:
        # Init
        
        super(TestCreateWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        
        # Button connections
        self.nerd_mode_button.clicked.connect(self.open_nerd_mode)
    
    # Button methods
    def open_nerd_mode(self) -> None:
        """Opens the nerd mode for making tests"""

        os.system(f"code \"{os.getcwd()}\\tests\"")


class TestRunWindow(QMainWindow, ui_test_run.Ui_main_window):
    def __init__(self) -> None:
        # Init
        
        super(TestRunWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
        self.display_tests()
        
        # Button connections
        self.test_run_button.clicked.connect(self.run_test)
        self.refresh_button.clicked.connect(self.display_tests)
    
    
    def display_tests(self) -> None:
        """Displays the tests to the list"""
        
        self.tests_list.clear()
        self.tests_list.addItems(tests.get_test_names())
    
    
    # Button methods   
    def run_test(self) -> None:
        """Run the selected test"""
        
        # Run only if there is a selected item
        if self.tests_list.currentItem():
            # Get grades and info
            grades = tests.run_test(self.tests_list.currentItem().text())
            info = tests.info_from_name(self.tests_list.currentItem().text())
            
            # Show results window
            test_results_window.show(info, grades)
            
            
class TestResultsWindow(QMainWindow, ui_test_results.Ui_main_window):
    def __init__(self) -> None:
        # Init
        
        super(TestResultsWindow, self).__init__()
        self.setupUi(self)
        self.setCentralWidget(self.main_frame)
    
    def show(self, info: dict, grades: dict) -> None:
        """Show the window with the relevant information"""
        
        # Clear items
        self.grades_list.clear()
        self.info_list.clear()
        
        # Set grades
        for name, grade in grades.items():
            self.grades_list.addItem(f"{name}: {float(grade * 100):.1f}%")
        
        # Add info
        for key, value in info.items():
            self.info_list.addItem(f"{key.replace('-', ' ').capitalize()}: {value}")
        
        super(TestResultsWindow, self).show()


def create_windows(app: QApplication) -> None:
    global start_window 
    global test_create_window
    global test_run_window
    global test_results_window
    
    start_window = StartWindow(app)
    test_create_window = TestCreateWindow()
    test_run_window = TestRunWindow()
    test_results_window = TestResultsWindow()