# main.py
# Py Grader
# Makes it easy to grade an assignment based on test cases


# Imports
import os
import sys

import src.gui as gui
from PySide6 import QtWidgets


# Definitions
def main() -> None:
    # Main
    
    # Add directories to path
    sys.path.append(os.path.abspath("turnins"))
    
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    
    # Create start window and show
    gui.create_windows(app)
    gui.start_window.show()
    
    # Start app and exit with code
    sys.exit(app.exec())


# Run
if __name__ == "__main__":
    main()