# main.pyw
# Py Grader
# Makes it easy to grade an assignment based on test cases


# Imports
import sys
from PySide6 import QtWidgets
import gui


# Definitions
def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    gui.create_windows()
    gui.start_window.show()
    sys.exit(app.exec())


# Run
if __name__ == "__main__":
    main()