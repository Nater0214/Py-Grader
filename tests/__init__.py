# tests/__init__.py
# Handles testing


# Imports
import importlib
import inspect
import os
import sys
from fractions import Fraction
from io import StringIO
from os import listdir

from . import test_root


# Definitions
class InvalidTestError(Exception): pass # An invalid test

def get_test_infos() -> list[dict]:
    """Get the info blocks of each test"""
    
    infos = [] # The infos
    
    # Get files and remove non-tests
    files = listdir("tests")
    files.remove("__pycache__")
    files.remove("__init__.py")
    files.remove("test_root.py")
    
    # Strip .py from each file and store in list
    tests = [file[:file.index('.py')] for file in files]
    
    # Loop through the tests and append their INFO to list
    for test in tests:
        test_module = importlib.import_module(f".{test}", __name__)
        
        test_module.INFO["file-name"] = test + '.py'
        try:
            infos.append(test_module.INFO)
        except AttributeError:
            infos.append("NO_INFO")
    
    # Return the INFOs
    return infos


def get_test_names() -> list[str]:
    """Return all the test names"""
    
    return [info["name"] for info in get_test_infos()]


def info_from_name(test_name: str) -> str:
    """Returns the info block of the test with a given name"""
    
    for info in get_test_infos():
        if info["name"] == test_name:
            return info    


def run_test(test_name: str) -> dict:
    """Run a test with a given test name"""
    
    # Get test info
    test_info = info_from_name(test_name)
    file_name = test_info["file-name"]
    test_for = test_info["for"]
    
    # Import test and get methods
    test_module = importlib.import_module(f".{file_name[:file_name.find('.py')]}", __name__)
    tests = [t[1] for t in [var for var in inspect.getmembers(test_module, lambda v: isinstance(v, test_root.BaseTest))]]
    tests: list[test_root.BaseTest]
    
    # Grades
    grades = {}                    # The grades dictionary with the students' grades as Fraction objects
    grade_denominator = len(tests) # The denominator of each grade; the amount of tests
    
    # Grade each student
    for student in listdir(turnin_path := os.path.join("turnins", test_for)):
        # Set the grade numerator
        grade_numerator = 0
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Try to run the program
        try:
            student_program = importlib.import_module(os.path.join(turnin_path, student, 'main').replace("\\", "."))
        
        # Set grade to 0 if it fails to run and move to next student
        except Exception:
            sys.stdout = old_stdout
            grades[student] = Fraction(0, grade_denominator)
            continue
        
        # Get captured stdout and reset stdout
        printed_output = sys.stdout.getvalue().split("\n")
        sys.stdout = old_stdout
        
        # Test all cases with program
        for test in tests:
            # Run test
            try:
                result = test.run(student_program, printed_output)
                
            # If the test fails to run raise InvalidTestError
            except Exception:
                raise InvalidTestError("Test method raised an exception")

            # Increment grade if test passes
            if result:
                grade_numerator += 1
        
        # Give student grade
        grades[student] = Fraction(grade_numerator, grade_denominator)
    
    return grades