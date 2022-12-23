# main.py
# Py Grader
# Makes it easy to grade an assignment based on test cases


# Imports
from sys import argv
from PySide6 import QtWidgets
import gui


# Definitions
def main() -> None:
    app = QtWidgets.QApplication(argv)
    main_window = gui.main_window()
    main_window.show()
    app.exec()


# Run
if __name__ == "__main__":
    main()